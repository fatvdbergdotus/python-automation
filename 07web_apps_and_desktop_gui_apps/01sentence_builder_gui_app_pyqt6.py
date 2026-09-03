# pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Function to create a sentence from the input text
def make_sentence():
    input_text = text.text()
    label.setText(input_text.capitalize() + ".")  # Capitalize the first letter and add a period at the end

# Create the application and main window
app = QApplication([])
window = QWidget()
window.setWindowTitle("Sentence Builder")

# Set up the layout (vertical layout)
layout = QVBoxLayout()

# Add elements to the layout
text = QLineEdit()
layout.addWidget(text)

button = QPushButton("Make Sentence")
button.clicked.connect(make_sentence)
layout.addWidget(button)

label = QLabel("")
layout.addWidget(label)

# Set the layout for the main window and show it
window.setLayout(layout)    
window.show()
app.exec()

