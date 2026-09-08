from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QLineEdit

import json

def look_up_word():
    for word, definition in window.dictionary_data.items():
        if input_field.text().lower() in word.lower():
            definition_label.setText(word+":\n"+definition[0])

app = QApplication([])

window = QWidget()
window.setWindowTitle("Dictionary app")

layout = QVBoxLayout()

window.setLayout(layout)

window.dictionary_data = []

with open("dictionary_data.json", "r", encoding="utf-8") as f:
    window.dictionary_data = json.load(f)

prompt_label = QLabel("Enter a word you want to look up in the dictionary")
layout.addWidget(prompt_label)

input_field = QLineEdit()
input_field.setPlaceholderText("Enter word...")
layout.addWidget(input_field)

lookup_button = QPushButton("Look up")
layout.addWidget(lookup_button)

lookup_button.clicked.connect(look_up_word)

definition_label = QLabel("")
layout.addWidget(definition_label)

window.show()
app.exec()