

# PDF to Markdown Converter

**Turn PDFs into clean, structured Markdown — fast, readable, and ready for knowledge systems.**

Most PDF converters dump text. This project aims higher: it **reconstructs document structure** and outputs Markdown that is actually usable—headers, lists, code blocks, tables, and layout that makes sense.

Whether you’re building a knowledge base, preparing technical documentation, exporting research papers, or feeding content into an LLM pipeline—this tool is designed to turn “PDF chaos” into **clean Markdown you can work with**.

---

## Why this exists

PDF is a final-form format. Great for printing. Terrible for:

* editing and reformatting
* documentation workflows
* analysis and summarization
* building searchable knowledge bases
* automation pipelines

This tool bridges that gap by converting PDFs into Markdown with **structure and readability preserved**, not just text extraction.

---

## Key Capabilities

### Smart conversion (structure-first)

* Detects **headers**, **sections**, **lists**, **code blocks**, and **tables**
* Preserves layout and hierarchy as readable Markdown
* Produces Markdown that is compatible with documentation tooling and LLM workflows

### GUI for real use (not just a script)

* Convert a **local PDF** or download one from a **URL**
* Configure conversion behavior and output settings
* See status and output flow clearly—designed for day-to-day usage

### Advanced controls

* Whitespace cleanup
* Merge short broken lines into natural paragraphs
* Show or hide page markers
* Auto-delete temporary files

### CLI + Batch conversion

* Convert a single PDF
* Convert an entire folder (batch processing)
* Practical for automation, pipelines, and back-office conversion jobs

### Open source and extensible

* Built to be customized and expanded
* Clean project layout and separation between conversion logic and UI

---

## Screenshot

![GUI Screenshot](Screenshot%202025-07-06%20at%2018.57.50.png)

---

## Output Example

```markdown
# Arxiv Org Document

*Converted from PDF on 2025-07-06 18:24:50*

## Page 1

### Abstract
This note is based on the summary of our book entitled "Non-perturbative field theory...
...
| Spin chain | Planar N = 4 SYM | High energy scattering in QCD |
| --- | --- | --- |
| Cyclic spin chain | Single trace operator | Reggeized gluons |
```

---

## Installation

```bash
git clone <repo-url>
cd pdf2md_app
```

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### GUI

```bash
python pdf2md_gui.py
```

Workflow:

* Select a local PDF or enter a URL
* Choose conversion options (headers, lists, code, page markers)
* Set output file name
* Click **Convert**
* Output Markdown is saved under `output/`

---

### Desktop App (macOS)

After building with PyInstaller, a macOS desktop app is created:

`dist/pdf2md_gui.app`

Run it like any standard app (double-click). No terminal needed.

By default:

* Markdown files are saved under the user’s **Downloads**
* Temporary files are managed automatically

Tip: Drag the app into **Applications** for convenient access.

---

### CLI

Convert a single file:

```bash
python convert_pdf_to_markdown.py myfile.pdf -o output/myfile.md
```

Convert an entire folder:

```bash
python convert_pdf_to_markdown.py -d /path/to/pdf/folder
```

---

## Requirements

* Python 3.7+
* PyPDF2
* pdfplumber
* markdown
* tkinter (often included with Python)
* PySide6
* (Optional) pdfminer.six, Pillow, tabula-py, tqdm

See `requirements.txt` for the full list.

---

## Project Structure

```
pdf2md_app/
│
├── convert_pdf_to_markdown.py   # Main conversion logic
├── pdf2md_gui.py                # GUI application
├── requirements.txt
├── LICENSE
├── output/                      # Generated Markdown files
├── temp_downloads/              # Temporary files (auto-deleted)
└── README.md
```

---

## Demo

Demo video: [YouTube](https://youtu.be/GZdxzbws6b8)

> Note: GitHub does not render iframes inside README.
> The embed below works in Markdown viewers that support HTML.

<p align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/GZdxzbws6b8" title="PDF2MD Demo" frameborder="0" allowfullscreen></iframe>
</p>

---

## License

MIT License — see `LICENSE`.

---

## Credits

Developed by **Nir Elmaliah**
GitHub: [TheKingHippopotamus](https://github.com/TheKingHippopotamus)

