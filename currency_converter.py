"""
This currency converter app uses PyQT6 for the GUI and www.x-rates.com to
grab the currencies using BeautifulSoup
"""

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QComboBox
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')

    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate.split(" ")[0])

    return rate

def show_currency():
    amount = float(text.text())
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    rate = get_currency(in_cur, target_cur)
    conversion = round(amount * rate, 2)
    result = f"{amount} {in_cur} is {conversion} {target_cur}"
    output_label.setText(str(result))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Currency Converter')

layout = QVBoxLayout()

in_combo = QComboBox()
currencies = ['USD', 'EUR', 'INR', 'GBP', 'AUD', 'CAD', 'SGD']
in_combo.addItems(currencies)
layout.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout.addWidget(target_combo)

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Convert')
layout.addWidget(btn)
btn.clicked.connect(show_currency)

output_label = QLabel('')
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()