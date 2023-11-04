import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget

class MemoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sweetheart Memory App")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.welcome_label = QLabel("Hi, Honey! Welcome to our memory app. Are you ready to start?", self)
        self.layout.addWidget(self.welcome_label)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.show_first_question)
        self.layout.addWidget(self.start_button)

        self.central_widget.setLayout(self.layout)

    def show_first_question(self):
        self.start_button.setDisabled(True)

        self.question_label = QLabel("When was the very first time we met? Write your answer...", self)
        self.layout.addWidget(self.question_label)

        self.answer_text = QTextEdit(self)
        self.answer_text.setPlaceholderText("Type your answer here...")
        self.answer_text.textChanged.connect(self.show_submit_button)
        self.layout.addWidget(self.answer_text)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.check_first_memory)
        self.submit_button.setDisabled(True)
        self.layout.addWidget(self.submit_button)

    def show_submit_button(self):
        self.submit_button.setDisabled(False)

    def check_first_memory(self):
        user_answer = self.answer_text.toPlainText().lower()
        memory_keywords = ["wedding", "parking", "lot", "present", "gift", "late"]

        if any(keyword in user_answer for keyword in memory_keywords):
            self.response_label = QLabel("You remembered correctly! It's amazing how long ago that memory is.", self)
        else:
            self.response_label = QLabel("That's not quite it. Try again! Remember we were both late to an event?", self)
        self.layout.addWidget(self.response_label)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.show_second_question)
        self.layout.addWidget(self.next_button)

    def show_second_question(self):
        self.question_label.setText("What is your most favorite memory from the past 5+ years we've been together? Write your answer...")

        self.answer_text.clear()
        self.response_label.clear()
        self.next_button.setDisabled(True)

        self.answer_text.textChanged.connect(self.show_second_submit_button)

    def show_second_submit_button(self):
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.show_final_message)
        self.layout.addWidget(self.submit_button)

    def show_final_message(self):
        final_message = QLabel("I remember that memory! It's a very fond one. I love you very much, Honey.", self)
        self.layout.addWidget(final_message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MemoryApp()
    window.show()
    sys.exit(app.exec_())
