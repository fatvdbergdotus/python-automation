# pip install pyqt6

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt6.QtWidgets import QComboBox

from bs4 import BeautifulSoup
import requests

# List of currencies (for demonstration purposes, only a few are included)
currencies = ["USD", "EUR", "GBP", "JPY", "AUD"]

# Function to get the currency rate from x-rates.com
def get_currency_rate(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    return float(rate.split(" ")[0])  # Extract the numeric part of the rate

# Function to convert currency
def show_currency():
    input_text = text.text()
    rate = get_currency_rate(combo_input_currency.currentText(), combo_output_currency.currentText())
    print(f"Rate: {rate}, Input: {input_text}")
    output.setText(str(rate*float(input_text)))

# Create the application and main window
app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency converter App")

# Set up the layout (vertical layout)
main_layout = QVBoxLayout()
layout_top = QHBoxLayout()
layout_bottom = QHBoxLayout()
layout_left = QVBoxLayout()
layout_right = QVBoxLayout()

main_layout.addLayout(layout_top)
main_layout.addLayout(layout_bottom)
layout_top.addLayout(layout_left)
layout_top.addLayout(layout_right)

# Add elements to the layout
combo_input_currency = QComboBox()
combo_input_currency.addItems(currencies)
combo_input_currency.setCurrentIndex(0)  # Set default selection to the first currency
layout_left.addWidget(combo_input_currency)

combo_output_currency = QComboBox()
combo_output_currency.addItems(currencies)
combo_output_currency.setCurrentIndex(1)  # Set default selection to the second currency
layout_left.addWidget(combo_output_currency)

text = QLineEdit("1")
layout_right.addWidget(text)

button = QPushButton("Convert Currency")
button.clicked.connect(show_currency)
layout_right.addWidget(button)

output = QLabel("")
layout_bottom.addWidget(output)

# Set the layout for the main window and show it
window.setLayout(main_layout)    
window.show()
app.exec()