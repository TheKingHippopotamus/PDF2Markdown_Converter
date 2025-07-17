import sys
import time
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QComboBox,
)
from PySide6.QtCore import QTimer
from PySide6.QtGui import QTextCursor

LOG_PATH = Path("log.txt")


class MonitorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF2MD Monitor - Activity & Error Log")
        self.setMinimumWidth(800)
        self.setMinimumHeight(500)
        self.setGeometry(0, 0, 600, 800)
        self.setStyleSheet(
            """
            QWidget { background-color: #232136; color: #e0def4; }
            QTextEdit, QLineEdit { background-color: #2a273f; color: #e0def4; border: 1px solid #444; }
            QLabel { color: #e0def4; }
            QPushButton { background-color: #393552; color: #e0def4; border: 1px solid #444; padding: 6px; }
            QPushButton:hover { background-color: #4f4a6d; }
            QComboBox { background-color: #2a273f; color: #e0def4; border: 1px solid #444; }
        """
        )
        self.init_ui()
        self.last_size = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_log)
        self.timer.start(1000)  # Every second

    def init_ui(self):
        layout = QVBoxLayout()
        # סטטוס כללי
        status_layout = QHBoxLayout()
        self.status_label = QLabel("Status: Monitoring log.txt ...")
        self.filter_box = QComboBox()
        self.filter_box.addItems(["All", "App1", "App2", "Error", "Info", "Step"])
        self.filter_box.currentIndexChanged.connect(self.update_log)
        status_layout.addWidget(self.status_label)
        status_layout.addWidget(QLabel("Filter:"))
        status_layout.addWidget(self.filter_box)
        layout.addLayout(status_layout)
        # תיבת לוג
        self.log_view = QTextEdit()
        self.log_view.setReadOnly(True)
        layout.addWidget(self.log_view)
        # כפתורים
        btn_layout = QHBoxLayout()
        clear_btn = QPushButton("Clear Log View")
        clear_btn.clicked.connect(self.clear_log_view)
        save_btn = QPushButton("Save Log to File")
        save_btn.clicked.connect(self.save_log)
        btn_layout.addWidget(clear_btn)
        btn_layout.addWidget(save_btn)
        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def update_log(self):
        if not LOG_PATH.exists():
            self.log_view.setPlainText("No log file found. Waiting for activity...")
            return
        with open(LOG_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()
        filter_val = self.filter_box.currentText()
        filtered = []
        for line in lines:
            if filter_val == "All" or filter_val.lower() in line.lower():
                filtered.append(line)
        self.log_view.setPlainText("".join(filtered))
        cursor = self.log_view.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.log_view.setTextCursor(cursor)

    def clear_log_view(self):
        self.log_view.clear()

    def save_log(self):
        save_path = str(Path.home() / f"pdf2md_monitor_log_{int(time.time())}.txt")
        with open(save_path, "w", encoding="utf-8") as f:
            f.write(self.log_view.toPlainText())
        self.status_label.setText(f"Log saved to: {save_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MonitorWindow()
    win.show()
    sys.exit(app.exec())
