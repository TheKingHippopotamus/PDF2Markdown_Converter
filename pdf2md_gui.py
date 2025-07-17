import sys
import requests
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFileDialog,
    QLineEdit,
    QCheckBox,
    QTextEdit,
    QProgressBar,
    QMessageBox,
    QTabWidget,
    QGroupBox,
)
from PySide6.QtCore import Qt, QThread, Signal
import os
import re

from convert_pdf_to_markdown import (
    PDFToMarkdownConverter,
    OllamaClient,
    split_markdown_to_chunks,
    count_tokens,
    log_event,
    clean_chunk_text,
    split_markdown_by_pages,
)

from tkinter import scrolledtext


class DownloadThread(QThread):
    progress = Signal(str)
    finished = Signal(bool, str)

    def __init__(self, url, output_path):
        super().__init__()
        self.url = url
        self.output_path = output_path

    def run(self):
        try:
            self.progress.emit(f"Downloading PDF from: {self.url}")

            # Add headers to mimic a real browser
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1",
            }

            # First try with headers
            response = requests.get(self.url, headers=headers, stream=True, timeout=30)

            # If still forbidden, try without headers
            if response.status_code == 403:
                self.progress.emit("403 error - trying without custom headers...")
                response = requests.get(self.url, stream=True, timeout=30)

            response.raise_for_status()

            # Check if content is actually a PDF
            content_type = response.headers.get("content-type", "").lower()
            if "pdf" not in content_type and not self.url.lower().endswith(".pdf"):
                self.progress.emit("Warning: Content doesn't appear to be a PDF")

            with open(self.output_path, "wb") as f:
                total_size = int(response.headers.get("content-length", 0))
                downloaded = 0

                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)

                        # Show progress for large files
                        if total_size > 0:
                            progress = (downloaded / total_size) * 100
                            self.progress.emit(
                                f"Downloaded: {downloaded}/{total_size} bytes ({progress:.1f}%)"
                            )

            self.progress.emit("Download completed successfully!")
            self.finished.emit(True, self.output_path)

        except Exception as e:
            error_msg = f"Download failed: {str(e)}"
            self.progress.emit(error_msg)
            self.finished.emit(False, error_msg)
            # Show error popup
            QMessageBox.critical(None, "Download Error", error_msg)
            # Log error to file in Downloads
            try:
                log_path = os.path.expanduser("~/Downloads/pdf2md_log.txt")
                with open(log_path, "a", encoding="utf-8") as logf:
                    logf.write(error_msg + "\n")
            except Exception:
                pass


class ConverterThread(QThread):
    progress = Signal(str)
    finished = Signal(bool, str)
    progress_percent = Signal(int)

    def __init__(self, pdf_path, output_path, config):
        super().__init__()
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.config = config

    def run(self):
        try:
            import pdfplumber

            converter = PDFToMarkdownConverter(self.config)
            self.progress.emit(f"Converting: {self.pdf_path}")
            self.progress.emit(f"Config keys: {list(self.config.keys())}")

            markdown_content = []
            title = Path(self.pdf_path).stem.replace("_", " ").title()
            markdown_content.append(f"# {title}")
            from datetime import datetime

            markdown_content.append(
                f"\n*Converted from PDF on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"
            )
            markdown_content.append("")

            with pdfplumber.open(self.pdf_path) as pdf:
                total_pages = len(pdf.pages)
                for page_num, page in enumerate(pdf.pages, 1):
                    self.progress.emit(f"Processing page {page_num}/{total_pages}...")
                    text = page.extract_text()
                    if text:
                        cleaned_text = converter.clean_text(text)
                        if cleaned_text:
                            markdown_lines = converter.process_text_block(
                                cleaned_text, page_num
                            )
                            markdown_content.extend(markdown_lines)
                    tables = converter.extract_tables(page)
                    for table in tables:
                        markdown_content.append(table)
                        markdown_content.append("")
                    images = converter.extract_images(page)
                    for image in images:
                        markdown_content.append(image)
                        markdown_content.append("")
                    percent = int((page_num / total_pages) * 100)
                    self.progress_percent.emit(percent)

            with open(self.output_path, "w", encoding="utf-8") as f:
                f.write("\n".join(markdown_content))

            self.finished.emit(True, self.output_path)
        except Exception as e:
            self.progress.emit(f"Conversion error: {str(e)}")
            self.finished.emit(False, str(e))


class PDF2MDGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF to Markdown Converter")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.setGeometry(620, 0, 600, 800)
        self.setStyleSheet(
            """
            QWidget { background-color: #232136; color: #e0def4; }
            QTextEdit, QLineEdit { background-color: #2a273f; color: #e0def4; border: 1px solid #444; }
            QLabel { color: #e0def4; }
            QPushButton { background-color: #393552; color: #e0def4; border: 1px solid #444; padding: 6px; }
            QPushButton:hover { background-color: #4f4a6d; }
            QComboBox, QCheckBox, QGroupBox { background-color: #232136; color: #e0def4; }
            QProgressBar { background-color: #2a273f; color: #e0def4; border: 1px solid #444; }
        """
        )

        # Set output directory to user's Downloads folder
        self.output_dir = Path(os.path.expanduser("~/Downloads"))
        self.output_dir.mkdir(exist_ok=True)

        self.init_ui()
        self.converter_thread = None
        self.download_thread = None
        self.temp_pdf_path = None

        # --- Chat session state ---
        self.chat_session = []  # [{'role': 'user'/'assistant', 'content': ...}]
        self.markdown_chunks = []  # List of markdown chunks
        self.ollama_client = OllamaClient()
        self.loaded_md_path = None

    def init_ui(self):
        layout = QVBoxLayout()

        # Create tab widget for different input methods
        self.tab_widget = QTabWidget()

        # Local file tab
        self.local_tab = QWidget()
        self.init_local_tab()
        self.tab_widget.addTab(self.local_tab, "Local File")

        # URL tab
        self.url_tab = QWidget()
        self.init_url_tab()
        self.tab_widget.addTab(self.url_tab, "Download from URL")

        # Chat tab
        self.chat_tab = QWidget()
        self.init_chat_tab()
        self.tab_widget.addTab(self.chat_tab, "Chat with PDF")

        layout.addWidget(self.tab_widget)

        # Output file selection (shared)
        out_group = QGroupBox("Output Settings")
        out_layout = QHBoxLayout()
        self.out_input = QLineEdit()
        self.out_input.setPlaceholderText(
            f"Output Markdown file (default: {self.output_dir}/...)"
        )
        out_btn = QPushButton("Browse")
        out_btn.clicked.connect(self.browse_output)
        out_layout.addWidget(QLabel("Output:"))
        out_layout.addWidget(self.out_input)
        out_layout.addWidget(out_btn)
        out_group.setLayout(out_layout)
        layout.addWidget(out_group)

        # Options
        options_group = QGroupBox("Conversion Options")
        options_layout = QHBoxLayout()
        self.cb_headers = QCheckBox("Detect Headers")
        self.cb_headers.setChecked(True)
        self.cb_lists = QCheckBox("Detect Lists")
        self.cb_lists.setChecked(True)
        self.cb_code = QCheckBox("Detect Code Blocks")
        self.cb_code.setChecked(True)
        self.cb_pages = QCheckBox("Page Numbers")
        self.cb_pages.setChecked(True)
        options_layout.addWidget(self.cb_headers)
        options_layout.addWidget(self.cb_lists)
        options_layout.addWidget(self.cb_code)
        options_layout.addWidget(self.cb_pages)
        options_group.setLayout(options_layout)
        layout.addWidget(options_group)

        # Cleanup options
        cleanup_group = QGroupBox("Cleanup Options")
        cleanup_layout = QHBoxLayout()
        self.cb_auto_delete = QCheckBox("Auto-delete temporary PDFs")
        self.cb_auto_delete.setToolTip(
            "Automatically delete downloaded PDF files after successful conversion"
        )
        cleanup_layout.addWidget(self.cb_auto_delete)
        cleanup_layout.addStretch()  # Add space to the right
        cleanup_group.setLayout(cleanup_layout)
        layout.addWidget(cleanup_group)

        # Start button
        self.start_btn = QPushButton("Convert")
        self.start_btn.clicked.connect(self.start_conversion)
        layout.addWidget(self.start_btn)

        # Chunkify button
        self.chunk_btn = QPushButton("Create Chunks from Markdown")
        self.chunk_btn.clicked.connect(self.create_chunks_from_markdown)
        layout.addWidget(self.chunk_btn)

        # Progress/status
        self.status = QTextEdit()
        self.status.setReadOnly(True)
        self.status.setFixedHeight(150)
        layout.addWidget(self.status)

        # Progress bar for conversion
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def init_local_tab(self):
        layout = QVBoxLayout()

        # PDF file selection
        file_layout = QHBoxLayout()
        self.file_input = QLineEdit()
        self.file_input.setPlaceholderText("Select PDF file...")
        file_btn = QPushButton("Browse")
        file_btn.clicked.connect(self.browse_pdf)
        file_layout.addWidget(QLabel("PDF File:"))
        file_layout.addWidget(self.file_input)
        file_layout.addWidget(file_btn)
        layout.addLayout(file_layout)

        self.local_tab.setLayout(layout)

    def init_url_tab(self):
        layout = QVBoxLayout()

        # URL input
        url_layout = QHBoxLayout()
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText(
            "Enter PDF URL (e.g., https://example.com/document.pdf)"
        )
        download_btn = QPushButton("Download")
        download_btn.clicked.connect(self.download_pdf)
        url_layout.addWidget(QLabel("PDF URL:"))
        url_layout.addWidget(self.url_input)
        url_layout.addWidget(download_btn)
        layout.addLayout(url_layout)

        # Download status
        self.download_status = QLabel("Enter a URL and click Download to fetch the PDF")
        layout.addWidget(self.download_status)

        self.url_tab.setLayout(layout)

    def init_chat_tab(self):
        layout = QVBoxLayout()
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.chat_input = QLineEdit()
        self.chat_input.setPlaceholderText("Ask a question about the PDF/Markdown...")
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_chat_message)
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.chat_input)
        input_layout.addWidget(send_btn)
        layout.addWidget(self.chat_history)
        layout.addLayout(input_layout)
        self.chat_tab.setLayout(layout)

    def send_chat_message(self):
        user_msg = self.chat_input.text().strip()
        if not user_msg:
            return
        self.chat_history.append(f"<b>You:</b> {user_msg}")
        self.chat_input.clear()
        self.chat_history.append("<i>Thinking...</i>")

        # Load Markdown file if not loaded
        if not self.loaded_md_path:
            # Try to get from output input
            md_path = self.out_input.text().strip()
            if not md_path or not Path(md_path).exists():
                self.chat_history.append(
                    "<span style='color:red'>No Markdown file loaded. Please convert a PDF first.</span>"
                )
                return
            self.loaded_md_path = md_path
            with open(md_path, "r", encoding="utf-8") as f:
                md_text = f.read()
            self.markdown_chunks = split_markdown_to_chunks(
                md_text, max_tokens=1800
            )  # 1800 to leave room for Q&A

        # RAG: חיפוש צ'אנקים רלוונטיים (פשוט: לפי הופעת מילים מהשאלה)
        relevant_chunks = []
        for chunk in self.markdown_chunks:
            if any(word.lower() in chunk.lower() for word in user_msg.split()):
                relevant_chunks.append(chunk)
        if not relevant_chunks:
            # אם לא נמצא, ניקח את הצ'אנק הראשון
            relevant_chunks = [self.markdown_chunks[0]]
        context = "\n\n".join(relevant_chunks)
        # בונים prompt מלא
        system_prompt = "You are an expert assistant. Answer questions based on the following document."
        prompt = f"Document:\n{context}\n\nQuestion: {user_msg}"
        # בונים היסטוריית שיחה
        messages = [{"role": "system", "content": system_prompt}]
        for m in self.chat_session:
            messages.append(m)
        messages.append({"role": "user", "content": prompt})
        # שולחים ל-Ollama
        answer = self.ollama_client.chat(messages)
        answer_clean = clean_llm_list_answer(answer)
        self.chat_history.append(f"<b>Assistant:</b> {answer_clean}")
        self.chat_session.append({"role": "user", "content": user_msg})
        self.chat_session.append({"role": "assistant", "content": answer})

    def browse_pdf(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Select PDF File", str(Path.home()), "PDF Files (*.pdf)"
        )
        if file:
            self.file_input.setText(file)

            # Suggest output file in output directory with original name
            pdf_path = Path(file)
            pdf_name = pdf_path.stem  # Get filename without extension
            out_file = str(self.output_dir / f"{pdf_name}.md")
            self.out_input.setText(out_file)

            # Show file selection message
            self.status.append(f"✓ Selected: {pdf_path.name}")
            self.status.append(f"✓ Output will be saved to: {out_file}")

    def download_pdf(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "Error", "Please enter a valid URL.")
            return
        # Better URL validation
        if not url.startswith(("http://", "https://")):
            QMessageBox.warning(self, "Error", "Please enter a valid HTTP/HTTPS URL.")
            return
        # Create temp directory in Downloads if it doesn't exist
        import os

        temp_dir = Path(os.path.expanduser("~/Downloads/temp_downloads"))
        try:
            temp_dir.mkdir(exist_ok=True)
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Could not create temp_downloads directory in Downloads: {e}",
            )
            return

        # Generate meaningful filename based on URL
        try:
            from urllib.parse import urlparse

            parsed_url = urlparse(url)

            # Try to extract filename from URL path
            path_parts = parsed_url.path.split("/")
            if path_parts and path_parts[-1].lower().endswith(".pdf"):
                # Use the actual filename from URL
                original_filename = path_parts[-1]
                base_name = Path(original_filename).stem
                filename = f"{base_name}.pdf"
            else:
                # Use domain name as base
                domain = parsed_url.netloc.replace(".", "_").replace("www_", "")
                filename = f"{domain}_document.pdf"
        except:
            # Fallback to hash-based name
            filename = f"downloaded_{hash(url) % 10000}.pdf"

        self.temp_pdf_path = str(temp_dir / filename)

        # Start download
        self.download_status.setText("Downloading...")
        self.download_thread = DownloadThread(url, self.temp_pdf_path)
        self.download_thread.progress.connect(self.status.append)
        self.download_thread.finished.connect(self.download_finished)
        self.download_thread.start()

    def download_finished(self, success, result):
        if success:
            if self.temp_pdf_path:
                downloaded_filename = Path(self.temp_pdf_path).name
                self.download_status.setText(f"Downloaded: {downloaded_filename}")

                # Suggest output file in output directory with meaningful name
                pdf_name = Path(self.temp_pdf_path).stem
                out_file = str(self.output_dir / f"{pdf_name}.md")
                self.out_input.setText(out_file)

                # Show success message with file locations
                self.status.append(f"✓ Downloaded: {downloaded_filename}")
                self.status.append(f"✓ Output will be saved to: {out_file}")
        else:
            self.download_status.setText("Download failed!")
            QMessageBox.warning(
                self, "Download Error", f"Failed to download PDF: {result}"
            )

    def browse_output(self):
        # Start in output directory by default
        default_path = str(self.output_dir)
        file, _ = QFileDialog.getSaveFileName(
            self, "Select Output Markdown File", default_path, "Markdown Files (*.md)"
        )
        if file:
            self.out_input.setText(file)

    def start_conversion(self):
        # Determine which input method is active
        current_tab = self.tab_widget.currentIndex()

        if current_tab == 0:  # Local file tab
            pdf_path = self.file_input.text().strip()
            if not pdf_path or not Path(pdf_path).exists():
                QMessageBox.warning(self, "Error", "Please select a valid PDF file.")
                return
        else:  # URL tab
            if not self.temp_pdf_path or not Path(self.temp_pdf_path).exists():
                QMessageBox.warning(
                    self, "Error", "Please download a PDF from URL first."
                )
                return
            pdf_path = self.temp_pdf_path

        output_path = self.out_input.text().strip()
        if not output_path:
            QMessageBox.warning(
                self, "Error", "Please specify an output Markdown file."
            )
            return

        # Get default config and override with GUI settings
        default_config = PDFToMarkdownConverter()._get_default_config()
        config = {
            **default_config,  # Include all default settings
            "detect_headers": self.cb_headers.isChecked(),
            "detect_lists": self.cb_lists.isChecked(),
            "detect_code_blocks": self.cb_code.isChecked(),
            "preserve_page_numbers": self.cb_pages.isChecked(),
        }

        self.status.clear()
        self.status.append("Starting conversion...")
        self.start_btn.setEnabled(False)
        self.progress_bar.setValue(0)
        self.converter_thread = ConverterThread(pdf_path, output_path, config)
        self.converter_thread.progress.connect(self.status.append)
        self.converter_thread.finished.connect(self.conversion_finished)
        self.converter_thread.progress_percent.connect(self.progress_bar.setValue)
        self.converter_thread.start()

    def conversion_finished(self, success, output_path):
        if success:
            self.status.append(f"\nSuccess! Markdown saved to: {output_path}")
            self.progress_bar.setValue(100)

            # Handle temporary PDF cleanup
            if self.temp_pdf_path and Path(self.temp_pdf_path).exists():
                if self.cb_auto_delete.isChecked():
                    # Auto-delete without asking
                    self.delete_temp_file()
                else:
                    # Ask user
                    self.ask_delete_temp_file()
        else:
            self.status.append("\nConversion failed.")
            self.progress_bar.setValue(0)
        self.start_btn.setEnabled(True)

    def delete_temp_file(self):
        """Delete temporary PDF file without asking."""
        if self.temp_pdf_path:
            temp_file = Path(self.temp_pdf_path)
            if temp_file.exists():
                try:
                    temp_file.unlink()  # Delete the file
                    self.status.append(
                        f"✓ Auto-deleted temporary file: {temp_file.name}"
                    )
                    self.temp_pdf_path = None  # Clear the reference
                except Exception as e:
                    self.status.append(f"⚠ Could not delete temporary file: {str(e)}")

    def ask_delete_temp_file(self):
        """Ask user if they want to delete the temporary PDF file."""
        if self.temp_pdf_path:
            temp_file = Path(self.temp_pdf_path)
            if temp_file.exists():
                reply = QMessageBox.question(
                    self,
                    "Delete Temporary File",
                    f"Conversion completed successfully!\n\n"
                    f"Would you like to delete the temporary PDF file?\n"
                    f"File: {temp_file.name}\n"
                    f"Location: {temp_file.parent}",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No,
                )

                if reply == QMessageBox.StandardButton.Yes:
                    self.delete_temp_file()
                else:
                    self.status.append(f"ℹ Kept temporary file: {temp_file.name}")

    def create_chunks_from_markdown(self):
        from PySide6.QtWidgets import QFileDialog, QMessageBox
        import json
        from utils.enrichment import enrich_text

        md_path, _ = QFileDialog.getOpenFileName(
            self, "Select Markdown File", str(self.output_dir), "Markdown Files (*.md)"
        )
        if not md_path:
            return
        with open(md_path, "r", encoding="utf-8") as f:
            md_text = f.read()
        # ניקוי סימנים לא רלוונטיים (אפשר להרחיב בהמשך)
        clean_text = md_text.replace("```", "").replace("#", "")
        # חלוקה לפי עמודים
        page_chunks = split_markdown_by_pages(clean_text)
        clean_chunks = [
            clean_chunk_text(chunk) for chunk in page_chunks if chunk.strip()
        ]
        # enrichment לכל צ'אנק
        enriched_chunks = [enrich_text(chunk) for chunk in clean_chunks]
        out_path = str(Path(md_path).with_name(Path(md_path).stem + "_chunks.json"))
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump({"chunks": enriched_chunks}, f, ensure_ascii=False, indent=2)
        QMessageBox.information(
            self, "Chunks Created", f"Chunked file saved to:\n{out_path}"
        )


def clean_llm_list_answer(text: str) -> str:
    """
    Clean and format LLM/model answers for readability:
    - Numbered/bulleted lists on separate lines
    - Fix broken lines
    - Remove extra spaces
    - Fix numbering issues (e.g., '1 0 .' -> '10.')
    """
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r" +", " ", text)
    # Combine broken lines within items
    text = re.sub(r"(?<=\w)\s*\n(?=[a-zA-Z])", " ", text)
    # Ensure each numbered/bullet item starts on a new line
    text = re.sub(r"(?<!\n)(\d+\.|\*\*|•)", r"\n\1", text)
    # Remove extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Fix double-digit numbers with space (e.g., '1 0 .' -> '10.')
    text = re.sub(r"(\d) (\d) \.", r"\1\2.", text)
    return text.strip()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDF2MDGui()
    window.show()
    sys.exit(app.exec())
