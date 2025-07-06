# PDF to Markdown Converter

## תיאור הפרויקט / Project Description

ממיר PDF למסמכי Markdown עם ממשק גרפי ידידותי למשתמש.
A PDF to Markdown converter with a user-friendly graphical interface.

## תכונות / Features

- המרת קבצי PDF למסמכי Markdown
- ממשק גרפי פשוט ונוח לשימוש
- שמירת התוצאות בתיקיית output
- תמיכה בקבצים מרובים

- Convert PDF files to Markdown documents
- Simple and user-friendly graphical interface
- Save results in output directory
- Support for multiple files

## התקנה / Installation

1. וודא שיש לך Python 3.7+ מותקן
   Make sure you have Python 3.7+ installed

2. התקן את התלויות הנדרשות
   Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## שימוש / Usage

### ממשק גרפי / Graphical Interface
```bash
python pdf2md_gui.py
```

### שורת פקודה / Command Line
```bash
python convert_pdf_to_markdown.py <pdf_file_path>
```

## מבנה הפרויקט / Project Structure

```
pdf2md_app/
├── convert_pdf_to_markdown.py  # Main conversion script
├── pdf2md_gui.py              # Graphical user interface
├── requirements.txt            # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
├── output/                    # Converted markdown files
└── temp_downloads/            # Temporary files
```

## דרישות מערכת / System Requirements

- Python 3.7+
- pip (Python package installer)
- תלויות נוספות מפורטות בקובץ requirements.txt
- Additional dependencies listed in requirements.txt

## רישיון / License

פרויקט זה זמין תחת רישיון MIT
This project is available under the MIT License

**מפתח / Developer:** [TheKingHippopotamus](https://github.com/TheKingHippopotamus)

## תרומה / Contributing

תרומות יתקבלו בברכה! אנא צור issue או pull request
Contributions are welcome! Please create an issue or pull request

## תמיכה / Support

אם יש לך שאלות או בעיות, אנא צור issue בפרויקט
If you have questions or issues, please create an issue in the project # PDF2Markdown_Converter
