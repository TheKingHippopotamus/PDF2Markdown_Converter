import sys
import requests
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QLineEdit, QCheckBox, QTextEdit, QProgressBar, QMessageBox,
    QTabWidget, QGroupBox
)
from PySide6.QtCore import Qt, QThread, Signal

from convert_pdf_to_markdown import PDFToMarkdownConverter

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
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            # First try with headers
            response = requests.get(self.url, headers=headers, stream=True, timeout=30)
            
            # If still forbidden, try without headers
            if response.status_code == 403:
                self.progress.emit("403 error - trying without custom headers...")
                response = requests.get(self.url, stream=True, timeout=30)
            
            response.raise_for_status()
            
            # Check if content is actually a PDF
            content_type = response.headers.get('content-type', '').lower()
            if 'pdf' not in content_type and not self.url.lower().endswith('.pdf'):
                self.progress.emit("Warning: Content doesn't appear to be a PDF")
            
            with open(self.output_path, 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        
                        # Show progress for large files
                        if total_size > 0:
                            progress = (downloaded / total_size) * 100
                            self.progress.emit(f"Downloaded: {downloaded}/{total_size} bytes ({progress:.1f}%)")
            
            self.progress.emit("Download completed successfully!")
            self.finished.emit(True, self.output_path)
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                error_msg = f"Access forbidden (403). The server is blocking direct downloads. Try:\n1. Opening the URL in a browser first\n2. Using a different PDF URL\n3. Downloading manually and using the 'Local File' tab"
            elif e.response.status_code == 404:
                error_msg = f"File not found (404). The PDF URL may be incorrect or the file has been moved."
            else:
                error_msg = f"HTTP Error {e.response.status_code}: {e.response.reason}"
            self.progress.emit(f"Download failed: {error_msg}")
            self.finished.emit(False, error_msg)
            
        except requests.exceptions.Timeout:
            error_msg = "Download timed out. The server is taking too long to respond."
            self.progress.emit(f"Download failed: {error_msg}")
            self.finished.emit(False, error_msg)
            
        except requests.exceptions.ConnectionError:
            error_msg = "Connection error. Please check your internet connection and try again."
            self.progress.emit(f"Download failed: {error_msg}")
            self.finished.emit(False, error_msg)
            
        except Exception as e:
            error_msg = f"Download failed: {str(e)}"
            self.progress.emit(error_msg)
            self.finished.emit(False, error_msg)

class ConverterThread(QThread):
    progress = Signal(str)
    finished = Signal(bool, str)

    def __init__(self, pdf_path, output_path, config):
        super().__init__()
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.config = config

    def run(self):
        try:
            converter = PDFToMarkdownConverter(self.config)
            self.progress.emit(f"Converting: {self.pdf_path}")
            self.progress.emit(f"Config keys: {list(self.config.keys())}")
            success = converter.convert_pdf_to_markdown(self.pdf_path, self.output_path)
            self.finished.emit(success, self.output_path)
        except Exception as e:
            self.progress.emit(f"Conversion error: {str(e)}")
            self.finished.emit(False, str(e))

class PDF2MDGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF to Markdown Converter")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        
        # Ensure output directory exists
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        
        self.init_ui()
        self.converter_thread = None
        self.download_thread = None
        self.temp_pdf_path = None

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
        
        layout.addWidget(self.tab_widget)

        # Output file selection (shared)
        out_group = QGroupBox("Output Settings")
        out_layout = QHBoxLayout()
        self.out_input = QLineEdit()
        self.out_input.setPlaceholderText(f"Output Markdown file (default: {self.output_dir}/...)")
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
        self.cb_auto_delete.setToolTip("Automatically delete downloaded PDF files after successful conversion")
        cleanup_layout.addWidget(self.cb_auto_delete)
        cleanup_layout.addStretch()  # Add space to the right
        cleanup_group.setLayout(cleanup_layout)
        layout.addWidget(cleanup_group)

        # Start button
        self.start_btn = QPushButton("Convert")
        self.start_btn.clicked.connect(self.start_conversion)
        layout.addWidget(self.start_btn)

        # Progress/status
        self.status = QTextEdit()
        self.status.setReadOnly(True)
        self.status.setFixedHeight(150)
        layout.addWidget(self.status)

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
        self.url_input.setPlaceholderText("Enter PDF URL (e.g., https://example.com/document.pdf)")
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

    def browse_pdf(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select PDF File", str(Path.home()), "PDF Files (*.pdf)")
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
        if not url.startswith(('http://', 'https://')):
            QMessageBox.warning(self, "Error", "Please enter a valid HTTP/HTTPS URL.")
            return
        
        # Create temp directory if it doesn't exist
        temp_dir = Path("temp_downloads")
        temp_dir.mkdir(exist_ok=True)
        
        # Generate meaningful filename based on URL
        try:
            from urllib.parse import urlparse
            parsed_url = urlparse(url)
            
            # Try to extract filename from URL path
            path_parts = parsed_url.path.split('/')
            if path_parts and path_parts[-1].lower().endswith('.pdf'):
                # Use the actual filename from URL
                original_filename = path_parts[-1]
                base_name = Path(original_filename).stem
                filename = f"{base_name}.pdf"
            else:
                # Use domain name as base
                domain = parsed_url.netloc.replace('.', '_').replace('www_', '')
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
            QMessageBox.warning(self, "Download Error", f"Failed to download PDF: {result}")

    def browse_output(self):
        # Start in output directory by default
        default_path = str(self.output_dir)
        file, _ = QFileDialog.getSaveFileName(self, "Select Output Markdown File", default_path, "Markdown Files (*.md)")
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
                QMessageBox.warning(self, "Error", "Please download a PDF from URL first.")
                return
            pdf_path = self.temp_pdf_path
        
        output_path = self.out_input.text().strip()
        if not output_path:
            QMessageBox.warning(self, "Error", "Please specify an output Markdown file.")
            return
        
        # Get default config and override with GUI settings
        default_config = PDFToMarkdownConverter()._get_default_config()
        config = {
            **default_config,  # Include all default settings
            'detect_headers': self.cb_headers.isChecked(),
            'detect_lists': self.cb_lists.isChecked(),
            'detect_code_blocks': self.cb_code.isChecked(),
            'preserve_page_numbers': self.cb_pages.isChecked(),
        }
        
        self.status.clear()
        self.status.append("Starting conversion...")
        self.start_btn.setEnabled(False)
        self.converter_thread = ConverterThread(pdf_path, output_path, config)
        self.converter_thread.progress.connect(self.status.append)
        self.converter_thread.finished.connect(self.conversion_finished)
        self.converter_thread.start()

    def conversion_finished(self, success, output_path):
        if success:
            self.status.append(f"\nSuccess! Markdown saved to: {output_path}")
            
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
        self.start_btn.setEnabled(True)

    def delete_temp_file(self):
        """Delete temporary PDF file without asking."""
        temp_file = Path(self.temp_pdf_path)
        if temp_file.exists():
            try:
                temp_file.unlink()  # Delete the file
                self.status.append(f"✓ Auto-deleted temporary file: {temp_file.name}")
                self.temp_pdf_path = None  # Clear the reference
            except Exception as e:
                self.status.append(f"⚠ Could not delete temporary file: {str(e)}")

    def ask_delete_temp_file(self):
        """Ask user if they want to delete the temporary PDF file."""
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
                QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.delete_temp_file()
            else:
                self.status.append(f"ℹ Kept temporary file: {temp_file.name}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDF2MDGui()
    window.show()
    sys.exit(app.exec()) 