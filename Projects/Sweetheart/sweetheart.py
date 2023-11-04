import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MemoryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sweetheart Memory App")
        self.setGeometry(100, 100, 800, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.welcome_label = QLabel("Hi, Hunny! Welcome to our memory app. Are you ready to start?", self)
        self.layout.addWidget(self.welcome_label)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.show_first_question)
        self.layout.addWidget(self.start_button)

        self.central_widget.setLayout(self.layout)
        self.answer_text = None  # Initialize answer_text as None

    def show_first_question(self):
        self.start_button.setDisabled(True)

        self.question_label = QLabel("When was the very first time we met? Write your answer...", self)
        self.layout.addWidget(self.question_label)

        self.answer_text = QTextEdit(self)
        self.answer_text.setPlaceholderText("Type your answer here...")
        self.layout.addWidget(self.answer_text)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.check_first_memory)
        self.layout.addWidget(self.submit_button)

        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.show_second_question)
        self.layout.addWidget(self.next_button)
        self.submit_button_clicked = False  # Track if the submit button is clicked

    def check_first_memory(self):
        user_answer = self.answer_text.toPlainText().lower()
        memory_keywords = ["wedding", "parking", "lot", "present", "gift", "late"]

        if any(keyword in user_answer for keyword in memory_keywords):
            self.response_label = QLabel("You remembered correctly! It's amazing how long ago that memory is.", self)
            self.submit_button.setDisabled(True)  # Disable the submit button after correct input
            self.submit_button.hide()  # Hide the submit button
            self.submit_button_clicked = True
        else:
            self.response_label = QLabel("That's not quite it. Try again! Remember we were both late to an event?", self)
        self.layout.addWidget(self.response_label)

    def show_second_question(self):
        self.question_label.setText("What is your most favorite memory from the past 5+ years we've been together?")

        if self.answer_text is not None:
            self.answer_text.clear()  # Clear the previous text
        self.response_label.clear()
        self.next_button.setDisabled(True)

        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.show_canned_response)
        self.layout.addWidget(self.submit_button)

    def show_canned_response(self):
        canned_response = QLabel("I love that memory! Err... well, I am programmed to say that. But ask me if I remember that memory juuuuust to make sure!", self)
        self.layout.addWidget(canned_response)
        
        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.show_image)
        self.layout.addWidget(self.next_button)

    def show_image(self):
        self.question_label.setText("Imagine all the memories we'll make with our little family we are growing!")

        self.pixmap = QPixmap("family.jpg")
        self.image_label = QLabel(self)
        self.image_label.setPixmap(self.pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setFixedSize(500, 700)
        self.layout.addWidget(self.image_label)

        self.next_button.setText("The End")
        self.next_button.clicked.connect(self.close_app)
        self.layout.addWidget(self.next_button)

    def close_app(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MemoryApp()
    window.show()
    sys.exit(app.exec_())
