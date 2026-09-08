from pathlib import Path
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QFileDialog
from PyQt6.QtCore import Qt

def select_files():
    window.filenames, _ = QFileDialog.getOpenFileNames(window, "Select files")
    filenames_label.setText("\n".join(window.filenames))
    delete_button.setEnabled(True)

def delete_files():
    for filename in window.filenames:
        path = Path(filename)
# uncomment the three lines below to really delete the files
#       with open(path, "wb") as file:
#           file.write(b'')
#       path.unlink()
        print("deleted " + str(path))   
    filenames_label.setText("Deletion successful")
    window.filenames=[]        
    delete_button.setEnabled(False)

app = QApplication([])

window = QWidget()
window.setWindowTitle("File Destroyer")

layout = QVBoxLayout()

window.setLayout(layout)

window.filenames = []

prompt_label = QLabel("Select the files you want to destroy. The files will be <font color='red'>deleted</font>.")
layout.addWidget(prompt_label)

open_button = QPushButton("Select files")
open_button.setToolTip("Select the files to open.")
open_button.setFixedWidth(120)
layout.addWidget(open_button, alignment=Qt.AlignmentFlag.AlignCenter)
open_button.clicked.connect(select_files)

delete_button = QPushButton("Delete files")
delete_button.setToolTip("Delete the selected files.")
delete_button.setFixedWidth(120)
layout.addWidget(delete_button, alignment=Qt.AlignmentFlag.AlignCenter)
delete_button.clicked.connect(delete_files)
delete_button.setEnabled(False)

filenames_label = QLabel("")
layout.addWidget(filenames_label)

window.show()
app.exec()