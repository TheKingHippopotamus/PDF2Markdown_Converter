#!/usr/bin/env python3
"""
Advanced PDF to Markdown Converter
A robust tool for converting PDF documents to well-formatted Markdown files.
"""

import pdfplumber
import argparse
import re
import os
import sys
from pathlib import Path
from typing import List, Dict, Optional, Tuple
import json
from datetime import datetime
import requests


LOG_FILE = "log.txt"


def log_event(source: str, event_type: str, message: str):
    """Log an event to the shared log file."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}][{source}][{event_type}] {message}\n")


def count_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text for LLM context window management.
    For simple estimation, splits by whitespace. For more accurate results, integrate with a tokenizer.
    """
    # TODO: Integrate with model-specific tokenizer if available
    return len(text.split())


def split_markdown_to_chunks(text: str, max_tokens: int = 2000) -> list:
    """
    Split markdown text into chunks, each not exceeding max_tokens.
    Prefer splitting at empty lines (paragraphs) or headers.
    """
    lines = text.split("\n")
    chunks = []
    current_chunk = []
    current_tokens = 0
    for line in lines:
        line_tokens = count_tokens(line)
        # If adding this line would exceed the limit, start a new chunk
        if current_tokens + line_tokens > max_tokens and current_chunk:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_tokens = 0
        current_chunk.append(line)
        current_tokens += line_tokens
    if current_chunk:
        chunks.append("\n".join(current_chunk))
    return chunks


def clean_chunk_text(text: str) -> str:
    """
    Clean chunk text: remove tables, links, phone numbers, and special characters.
    """
    # Remove markdown tables (lines with | and ---)
    lines = text.split("\n")
    lines = [l for l in lines if not (l.strip().startswith("|") or "---" in l)]
    text = "\n".join(lines)
    # Remove URLs
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # Markdown links
    # Remove phone numbers (simple patterns)
    text = re.sub(r"\b\d{2,4}[-.\s]?\d{3}[-.\s]?\d{3,4}\b", "", text)
    # Remove emails
    text = re.sub(r"\b[\w.-]+@[\w.-]+\.\w+\b", "", text)
    # Remove special characters (except basic punctuation)
    text = re.sub(r'[^\w\s.,;:!?\-\'"()\[\]]+', "", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def split_markdown_by_pages(text: str) -> list:
    """
    Split markdown text into chunks by any occurrence of 'Page X of Y' (case-insensitive), excluding the marker.
    Ignore any text before the first page marker.
    """
    # מצא את כל המופעים של Page X of Y
    pattern = re.compile(r"Page\s*\d+\s*of\s*\d+", re.IGNORECASE)
    matches = list(pattern.finditer(text))
    chunks = []
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
    return chunks


class OllamaClient:
    """
    Simple client for interacting with Ollama's HTTP API.
    """

    def __init__(
        self, model: str = "aya-expanse:8b", host: str = "http://localhost:11434"
    ):
        self.model = model
        self.host = host.rstrip("/")

    def chat(self, messages: list) -> str:
        """
        Send a chat completion request to Ollama.
        messages: list of {"role": "user"/"assistant", "content": str}
        Returns: assistant's reply as string
        """
        url = f"{self.host}/api/chat"
        payload = {"model": self.model, "messages": messages}
        try:
            resp = requests.post(url, json=payload, timeout=60)
            resp.raise_for_status()
            # נסה לפענח stream של JSON
            try:
                lines = resp.text.strip().splitlines()
                if len(lines) > 1:
                    contents = []
                    for line in lines:
                        try:
                            data = json.loads(line)
                            contents.append(data.get("message", {}).get("content", ""))
                        except Exception:
                            continue
                    return "\n".join(contents)
                # אחרת, JSON רגיל
                data = resp.json()
                return data.get("message", {}).get("content", "")
            except Exception:
                return resp.text
        except Exception as e:
            return f"[Ollama error: {e}]"


class PDFToMarkdownConverter:
    """Advanced PDF to Markdown converter with intelligent text processing."""

    def __init__(self, config: Optional[Dict] = None):
        """Initialize the converter with optional configuration."""
        self.config = config or self._get_default_config()
        self.text_blocks = []
        self.current_page = 0

    def _get_default_config(self) -> Dict:
        """Get default configuration settings."""
        return {
            "preserve_page_numbers": True,
            "detect_headers": True,
            "detect_lists": True,
            "detect_code_blocks": True,
            "clean_whitespace": True,
            "merge_short_lines": True,
            "min_line_length": 40,
            "header_patterns": [
                r"^[A-Z][A-Z\s]{2,}$",  # ALL CAPS headers
                r"^\d+\.\s+[A-Z]",  # Numbered headers
                r"^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$",  # Title Case headers
            ],
            "list_patterns": [
                r"^\s*[-•*]\s+",  # Bullet lists
                r"^\s*\d+\.\s+",  # Numbered lists
                r"^\s*[a-z]\)\s+",  # Letter lists
            ],
            "code_patterns": [
                r"^```[\w]*$",  # Code block markers
                r"^\s*[a-zA-Z_][a-zA-Z0-9_]*\s*[:=]\s*",  # Variable assignments
                r'^\s*[<>/{}()[\]"\']+',  # HTML/XML tags or brackets
            ],
        }

    def clean_text(self, text: str) -> str:
        """Clean and normalize text content."""
        if not text:
            return ""

        # Remove excessive whitespace
        if self.config["clean_whitespace"]:
            text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
            text = re.sub(r" +", " ", text)
            text = re.sub(r"\t+", " ", text)

        # Merge short lines
        if self.config["merge_short_lines"]:
            lines = text.split("\n")
            merged_lines = []
            current_line = ""

            for line in lines:
                line = line.strip()
                if not line:
                    if current_line:
                        merged_lines.append(current_line)
                        current_line = ""
                    merged_lines.append("")
                elif len(line) < self.config["min_line_length"] and not self._is_header(
                    line
                ):
                    current_line += " " + line if current_line else line
                else:
                    if current_line:
                        merged_lines.append(current_line)
                    current_line = line

            if current_line:
                merged_lines.append(current_line)

            text = "\n".join(merged_lines)

        return text.strip()

    def _is_header(self, line: str) -> bool:
        """Check if a line appears to be a header."""
        if not self.config["detect_headers"]:
            return False

        for pattern in self.config["header_patterns"]:
            if re.match(pattern, line.strip()):
                return True
        return False

    def _is_list_item(self, line: str) -> bool:
        """Check if a line appears to be a list item."""
        if not self.config["detect_lists"]:
            return False

        for pattern in self.config["list_patterns"]:
            if re.match(pattern, line):
                return True
        return False

    def _is_code_block(self, line: str) -> bool:
        """Check if a line appears to be code."""
        if not self.config["detect_code_blocks"]:
            return False

        for pattern in self.config["code_patterns"]:
            if re.match(pattern, line.strip()):
                return True
        return False

    def _convert_header(self, line: str) -> str:
        """Convert a line to appropriate markdown header level."""
        line = line.strip()

        # Determine header level based on patterns
        if re.match(r"^[A-Z][A-Z\s]{2,}$", line):  # ALL CAPS
            return f"# {line}"
        elif re.match(r"^\d+\.\s+[A-Z]", line):  # Numbered
            return f"## {line}"
        elif re.match(r"^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*$", line):  # Title Case
            return f"### {line}"
        else:
            return f"## {line}"

    def _convert_list_item(self, line: str) -> str:
        """Convert a line to markdown list item."""
        line = line.strip()

        # Replace different bullet types with standard markdown
        line = re.sub(r"^\s*[-•*]\s+", "- ", line)
        line = re.sub(r"^\s*\d+\.\s+", "1. ", line)
        line = re.sub(r"^\s*[a-z]\)\s+", "- ", line)

        return line

    def _convert_code_block(self, line: str) -> str:
        """Convert a line to markdown code block."""
        return f"```\n{line}\n```"

    def process_text_block(self, text: str, page_num: int) -> List[str]:
        """Process a text block and convert to markdown lines."""
        if not text:
            return []

        lines = []
        if self.config["preserve_page_numbers"]:
            lines.append(f"\n## Page {page_num}\n")

        # Split into lines and process each
        text_lines = text.split("\n")
        in_code_block = False

        for line in text_lines:
            line = line.strip()
            if not line:
                lines.append("")
                continue

            # Check for code block markers
            if re.match(r"^```[\w]*$", line):
                in_code_block = not in_code_block
                lines.append(line)
                continue

            # Process based on content type
            if in_code_block:
                lines.append(line)
            elif self._is_header(line):
                lines.append(self._convert_header(line))
            elif self._is_list_item(line):
                lines.append(self._convert_list_item(line))
            elif self._is_code_block(line):
                lines.append(self._convert_code_block(line))
            else:
                lines.append(line)

        return lines

    def extract_tables(self, page) -> List[str]:
        """Extract and convert tables to markdown format."""
        tables = []
        extracted_tables = page.extract_tables()

        for table in extracted_tables:
            if not table or not table[0]:
                continue

            # Convert table to markdown
            markdown_table = []

            # Add header
            header = (
                "| " + " | ".join(str(cell) if cell else "" for cell in table[0]) + " |"
            )
            markdown_table.append(header)

            # Add separator
            separator = "| " + " | ".join("---" for _ in table[0]) + " |"
            markdown_table.append(separator)

            # Add data rows
            for row in table[1:]:
                if row:
                    data_row = (
                        "| "
                        + " | ".join(str(cell) if cell else "" for cell in row)
                        + " |"
                    )
                    markdown_table.append(data_row)

            tables.append("\n".join(markdown_table))

        return tables

    def extract_images(self, page) -> List[str]:
        """Extract image references and convert to markdown."""
        images = []
        # Note: pdfplumber doesn't directly extract images, but we can detect image areas
        # This is a placeholder for future enhancement
        return images

    def convert_pdf_to_markdown(
        self, pdf_path: str, output_path: Optional[str] = None
    ) -> bool:
        """Convert PDF to Markdown with advanced processing."""

        if not os.path.exists(pdf_path):
            print(f"Error: PDF file not found at {pdf_path}")
            return False

        if output_path is None:
            pdf_file = Path(pdf_path)
            output_path = str(pdf_file.with_suffix(".md"))

        try:
            markdown_content = []

            # Add document header
            title = Path(pdf_path).stem.replace("_", " ").title()
            markdown_content.append(f"# {title}")
            markdown_content.append(
                f"\n*Converted from PDF on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
            )
            markdown_content.append("")

            with pdfplumber.open(pdf_path) as pdf:
                total_pages = len(pdf.pages)
                print(f"Processing PDF with {total_pages} pages...")

                for page_num, page in enumerate(pdf.pages, 1):
                    print(f"Processing page {page_num}/{total_pages}...")

                    # Extract text
                    text = page.extract_text()
                    if text:
                        cleaned_text = self.clean_text(text)
                        if cleaned_text:
                            markdown_lines = self.process_text_block(
                                cleaned_text, page_num
                            )
                            markdown_content.extend(markdown_lines)

                    # Extract tables
                    tables = self.extract_tables(page)
                    for table in tables:
                        markdown_content.append(table)
                        markdown_content.append("")

                    # Extract images (placeholder)
                    images = self.extract_images(page)
                    for image in images:
                        markdown_content.append(image)
                        markdown_content.append("")

            # Write to markdown file
            with open(output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(markdown_content))

            print(f"Successfully converted PDF to Markdown: {output_path}")
            return True

        except Exception as e:
            print(f"Error processing PDF: {str(e)}")
            return False

    def batch_convert(
        self, input_dir: str, output_dir: Optional[str] = None
    ) -> Dict[str, bool]:
        """Convert multiple PDF files in a directory."""
        input_path = Path(input_dir)
        if not input_path.exists() or not input_path.is_dir():
            print(f"Error: Input directory not found: {input_dir}")
            return {}

        if output_dir is None:
            output_path = input_path / "markdown_output"
        else:
            output_path = Path(output_dir)

        output_path.mkdir(exist_ok=True)

        pdf_files = list(input_path.glob("*.pdf"))
        results = {}

        print(f"Found {len(pdf_files)} PDF files to convert...")

        for pdf_file in pdf_files:
            output_file = output_path / f"{pdf_file.stem}.md"
            print(f"\nConverting {pdf_file.name}...")

            success = self.convert_pdf_to_markdown(str(pdf_file), str(output_file))
            results[str(pdf_file)] = success

        return results


def main():
    """Main function with command-line interface."""
    parser = argparse.ArgumentParser(
        description="Advanced PDF to Markdown Converter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf                    # Convert single file
  %(prog)s document.pdf -o output.md      # Specify output file
  %(prog)s -d /path/to/pdfs              # Batch convert directory
  %(prog)s -c config.json document.pdf   # Use custom config
        """,
    )

    parser.add_argument("input", nargs="?", help="Input PDF file or directory")
    parser.add_argument("-o", "--output", help="Output markdown file")
    parser.add_argument("-d", "--directory", help="Batch convert all PDFs in directory")
    parser.add_argument("-c", "--config", help="Configuration JSON file")
    parser.add_argument(
        "--no-page-numbers", action="store_true", help="Disable page number headers"
    )
    parser.add_argument(
        "--no-headers", action="store_true", help="Disable header detection"
    )
    parser.add_argument(
        "--no-lists", action="store_true", help="Disable list detection"
    )
    parser.add_argument(
        "--no-code", action="store_true", help="Disable code block detection"
    )
    parser.add_argument(
        "--min-line-length",
        type=int,
        default=40,
        help="Minimum line length for merging",
    )

    args = parser.parse_args()

    # Always start with default config, then update with loaded config and CLI overrides
    default_config = PDFToMarkdownConverter()._get_default_config()
    config = {**default_config, **(args.config and json.load(open(args.config)) or {})}

    if args.no_page_numbers:
        config["preserve_page_numbers"] = False
    if args.no_headers:
        config["detect_headers"] = False
    if args.no_lists:
        config["detect_lists"] = False
    if args.no_code:
        config["detect_code_blocks"] = False
    if args.min_line_length:
        config["min_line_length"] = args.min_line_length

    # Create converter
    converter = PDFToMarkdownConverter(config)

    # Process based on arguments
    if args.directory:
        results = converter.batch_convert(args.directory, args.output)
        success_count = sum(1 for success in results.values() if success)
        print(
            f"\nBatch conversion complete: {success_count}/{len(results)} files converted successfully"
        )
        return 0 if success_count == len(results) else 1

    elif args.input:
        success = converter.convert_pdf_to_markdown(args.input, args.output)
        return 0 if success else 1

    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
