# PDF to Markdown Converter | ממיר PDF ל-Markdown

---

## תיאור בעברית | Description in English


מערכת מתקדמת להמרת מסמכי PDF לקבצי Markdown בפורמט קריא, כולל תמיכה בזיהוי כותרות, רשימות, קטעי קוד, טבלאות, וממשק גרפי נוח.


An advanced system for converting PDF documents to readable Markdown files, including support for headers, lists, code blocks, tables, and a user-friendly GUI.

![GUI Screenshot](Screenshot%202025-07-06%20at%2018.57.50.png)

---

## תכונות עיקריות | Key Features


- **המרה חכמה של PDF ל-Markdown**: זיהוי כותרות, רשימות, קוד, טבלאות, ושמירה על מבנה המסמך.
- **ממשק גרפי (GUI)**: מאפשר בחירת קובץ מקומי או הורדה מ-URL, קביעת אפשרויות המרה, ותצוגת סטטוס.
- **אפשרויות מתקדמות**: ניקוי רווחים, מיזוג שורות קצרות, שמירה/הסתרת מספרי עמודים, מחיקת קבצים זמניים אוטומטית.
- **תמיכה בהמרה אצוויתית**: המרת תיקיות שלמות של קבצי PDF (דרך CLI).
- **קוד פתוח, גמיש, וניתן להרחבה**.


- **Smart PDF to Markdown conversion**: Detects headers, lists, code, tables, and preserves document structure.
- **Graphical User Interface (GUI)**: Choose local file or download from URL, set conversion options, and view status.
- **Advanced options**: Whitespace cleanup, merge short lines, show/hide page numbers, auto-delete temp files.
- **Batch conversion support**: Convert entire folders of PDFs (via CLI).
- **Open source, flexible, and extensible.**

---

## דוגמת פלט | Output Example

```markdown
# Arxiv Org Document

*Converted from PDF on 2025-07-06 18:24:50*

## Page 1

### Abstract
This note is based on the summary of our book entitled "Non-perturbative field theory...
...
| Spin chain | Planar N = 4 SYM | High energy scattering in QCD |
| --- | --- | --- |
| Cyclic spin chain | Single trace operator | Reggeized guons |
```

---

## התקנה | Installation


1. **שכפול הריפוזיטורי:**
   ```bash
   git clone <repo-url>
   cd pdf2md_app
   ```
2. **התקנת סביבת פייתון מומלצת (Python 3.7+):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **התקנת התלויות:**
   ```bash
   pip install -r requirements.txt
   ```


1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd pdf2md_app
   ```
2. **(Recommended) Create a Python 3.7+ virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## שימוש | Usage

### ממשק גרפי (GUI) | GUI

#
```bash
python pdf2md_gui.py
```
- בחר קובץ PDF מקומי או הזן URL.
- בחר אפשרויות המרה (כותרות, רשימות, קוד, מספרי עמודים).
- קבע שם קובץ פלט.
- לחץ "Convert" – קובץ Markdown יישמר בתיקיית `output/`.

#
```bash
python pdf2md_gui.py
```
- Select a local PDF file or enter a URL.
- Choose conversion options (headers, lists, code, page numbers).
- Set output file name.
- Click "Convert" – Markdown file will be saved in the `output/` folder.

### שורת פקודה (CLI) | Command Line

#
```bash
python convert_pdf_to_markdown.py <קובץ.pdf> -o <פלט.md>
```
- דוגמאות:
  - המרת קובץ בודד:
    ```bash
    python convert_pdf_to_markdown.py myfile.pdf -o output/myfile.md
    ```
  - המרת תיקיה שלמה:
    ```bash
    python convert_pdf_to_markdown.py -d /path/to/pdf/folder
    ```

#
```bash
python convert_pdf_to_markdown.py <file.pdf> -o <output.md>
```
- Examples:
  - Convert a single file:
    ```bash
    python convert_pdf_to_markdown.py myfile.pdf -o output/myfile.md
    ```
  - Convert an entire folder:
    ```bash
    python convert_pdf_to_markdown.py -d /path/to/pdf/folder
    ```

---

## דרישות | Requirements

- Python 3.7+
- PyPDF2
- pdfplumber
- markdown
- tkinter (for GUI, usually included with Python)
- PySide6 (for GUI)
- (Optional) pdfminer.six, Pillow, tabula-py, tqdm

ראה `requirements.txt` לכל התלויות. | See `requirements.txt` for all dependencies.

---

## מבנה הפרויקט | Project Structure

```
pdf2md_app/
│
├── convert_pdf_to_markdown.py   # לוגיקת ההמרה הראשית | Main conversion logic
├── pdf2md_gui.py                # ממשק גרפי | GUI
├── requirements.txt
├── LICENSE
├── output/                      # קבצי Markdown שנוצרו | Output Markdown files
├── temp_downloads/              # קבצים זמניים (נמחקים אוטומטית) | Temporary files (auto-deleted)
└── README.md
```

---

## רישיון | License


This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## קרדיטים | Credits


- Developed by [TheKingHippopotamus](https://github.com/TheKingHippopotamus)
- Demo video: [YouTube](https://youtu.be/GZdxzbws6b8)


Nir Elmaliah
---

