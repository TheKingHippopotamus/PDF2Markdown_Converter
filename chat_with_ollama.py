import sys
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
    QTextEdit,
    QMessageBox,
)
from convert_pdf_to_markdown import OllamaClient, split_markdown_to_chunks, log_event
import json


class ChatWithOllama(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat with Ollama (PDF Chunks)")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.ollama_client = OllamaClient()
        self.chat_session = []
        self.chunks = []
        self.loaded_chunk_path = None
        self.setGeometry(1240, 0, 600, 800)
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

    def init_ui(self):
        layout = QVBoxLayout()
        # קובץ צ'אנקים
        file_layout = QHBoxLayout()
        self.chunk_input = QLineEdit()
        self.chunk_input.setPlaceholderText("Select chunked Markdown file...")
        file_btn = QPushButton("Browse")
        file_btn.clicked.connect(self.browse_chunk_file)
        file_layout.addWidget(QLabel("Chunks File:"))
        file_layout.addWidget(self.chunk_input)
        file_layout.addWidget(file_btn)
        layout.addLayout(file_layout)
        # תיבת שיחה
        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        layout.addWidget(self.chat_history)
        # קלט שאלה
        input_layout = QHBoxLayout()
        self.chat_input = QLineEdit()
        self.chat_input.setPlaceholderText("Ask a question about the document...")
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_chat_message)
        input_layout.addWidget(self.chat_input)
        input_layout.addWidget(send_btn)
        layout.addLayout(input_layout)
        self.setLayout(layout)

    def browse_chunk_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Chunked File", str(Path.home()), "Chunk Files (*.md *.json)"
        )
        if not path:
            return
        self.chunk_input.setText(path)
        self.loaded_chunk_path = path
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            # תמיכה במבנה {'chunks': [...]}
            if (
                isinstance(data, dict)
                and "chunks" in data
                and isinstance(data["chunks"], list)
            ):
                # תמיכה בצ'אנקים מועשרים (dict עם text, entities, keywords, summary)
                if all(isinstance(x, dict) and "text" in x for x in data["chunks"]):
                    self.chunks = data["chunks"]
                else:
                    self.chunks = [
                        x.strip()
                        for x in data["chunks"]
                        if isinstance(x, str) and x.strip()
                    ]
            # תומך גם ברשימת מחרוזות וגם ברשימת אובייקטים עם 'text'
            elif isinstance(data, list):
                if all(isinstance(x, str) for x in data):
                    self.chunks = [x.strip() for x in data if x.strip()]
                elif all(isinstance(x, dict) and "text" in x for x in data):
                    self.chunks = data
                else:
                    self.chat_history.append(
                        "<span style='color:red'>Unsupported JSON structure.</span>"
                    )
                    self.chunks = []
            else:
                self.chat_history.append(
                    "<span style='color:red'>Unsupported JSON structure.</span>"
                )
                self.chunks = []
        else:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
                self.chunks = [c.strip() for c in text.split("--- chunk") if c.strip()]
        self.chat_history.append(
            f"<span style='color:green'>Loaded {len(self.chunks)} chunks from file.</span>"
        )
        log_event(
            "App2", "Step", f"Loaded chunked file {path} ({len(self.chunks)} chunks)"
        )

    def send_chat_message(self):
        user_msg = self.chat_input.text().strip()
        if not user_msg:
            return
        self.chat_history.append(f"<b>You:</b> {user_msg}")
        self.chat_input.clear()
        self.chat_history.append("<i>Thinking...</i>")
        if not self.chunks:
            self.chat_history.append(
                "<span style='color:red'>No chunked file loaded.</span>"
            )
            return
        # RAG פשוט: חיפוש צ'אנקים רלוונטיים
        relevant_chunks = []
        for chunk in self.chunks:
            chunk_text = (
                chunk["text"] if isinstance(chunk, dict) and "text" in chunk else chunk
            )
            if isinstance(chunk_text, str) and any(
                word.lower() in chunk_text.lower() for word in user_msg.split()
            ):
                relevant_chunks.append(chunk)
        if not relevant_chunks:
            relevant_chunks = [self.chunks[0]]
        # בחר רק את הצ'אנק הרלוונטי ביותר (הראשון)
        best_chunk = relevant_chunks[0]
        # הצגת enrichment (אם קיים) למשתמש בלבד
        if isinstance(best_chunk, dict):
            info = []
            if best_chunk.get("summary"):
                info.append(f"<b>Summary:</b> {best_chunk['summary']}")
            if best_chunk.get("entities"):
                ents = ", ".join(
                    f"{e['text']} [{e['label']}]" for e in best_chunk["entities"]
                )
                info.append(f"<b>Entities:</b> {ents}")
            if best_chunk.get("keywords"):
                kws = ", ".join(best_chunk["keywords"])
                info.append(f"<b>Keywords:</b> {kws}")
            if info:
                self.chat_history.append(
                    "<div style='color:#a6e3a1'>" + "<br>".join(info) + "</div>"
                )
        # שלח למודל רק את ה-text של הצ'אנק
        context = (
            best_chunk["text"]
            if isinstance(best_chunk, dict) and isinstance(best_chunk.get("text"), str)
            else best_chunk
        )
        system_prompt = "You are an expert assistant. Answer questions based on the following document."
        prompt = f"Document:\n{context}\n\nQuestion: {user_msg}"
        messages = [{"role": "system", "content": system_prompt}]
        for m in self.chat_session:
            messages.append(m)
        messages.append({"role": "user", "content": prompt})
        try:
            answer = self.ollama_client.chat(messages)
            self.chat_history.append(f"<b>Assistant:</b> {answer}")
            self.chat_session.append({"role": "user", "content": user_msg})
            self.chat_session.append({"role": "assistant", "content": answer})
            log_event("App2", "Step", "User sent question ...")
        except json.JSONDecodeError as e:
            self.chat_history.append(
                f"<span style='color:red'>Ollama JSON error: {e}</span>"
            )
            self.chat_history.append(
                f"<span style='color:orange'>Raw response:</span> {answer}"
            )
            log_event("App2", "Error", f"Ollama JSON error: {e} | Raw: {answer}")
        except Exception as e:
            self.chat_history.append(f"<span style='color:red'>Error: {e}</span>")
            log_event("App2", "Error", f"Ollama error ...: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ChatWithOllama()
    win.show()
    sys.exit(app.exec())
