import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import requests


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Конвертер валют")
        self.setWindowIcon(QIcon("../icons8-получить-доллары-наличными-64.png"))

        self.ui.input_amount.setPlaceholderText("У меня есть:")
        self.ui.output_currency.setPlaceholderText("Получу:")
        self.ui.pushButton.clicked.connect(self.converter)

        self.add_functions()

    def add_functions(self):
        self.ui.pushButton_11.clicked.connect(lambda: self.write_number(self.ui.pushButton_11.text()))
        self.ui.pushButton_8.clicked.connect(lambda: self.write_number(self.ui.pushButton_8.text()))
        self.ui.pushButton_9.clicked.connect(lambda: self.write_number(self.ui.pushButton_9.text()))
        self.ui.pushButton_10.clicked.connect(lambda: self.write_number(self.ui.pushButton_10.text()))
        self.ui.pushButton_5.clicked.connect(lambda: self.write_number(self.ui.pushButton_5.text()))
        self.ui.pushButton_6.clicked.connect(lambda: self.write_number(self.ui.pushButton_6.text()))
        self.ui.pushButton_7.clicked.connect(lambda: self.write_number(self.ui.pushButton_7.text()))
        self.ui.pushButton_2.clicked.connect(lambda: self.write_number(self.ui.pushButton_2.text()))
        self.ui.pushButton_3.clicked.connect(lambda: self.write_number(self.ui.pushButton_3.text()))
        self.ui.pushButton_4.clicked.connect(lambda: self.write_number(self.ui.pushButton_4.text()))

    def write_number(self, number):
        a = self.ui.input_amount.text()
        self.ui.input_amount.setText(a + number)

    def converter(self):
        value1 = self.ui.comboBox.currentText()
        value2 = self.ui.comboBox_2.currentText()
        sum = self.ui.input_amount.text()
        print(value1, value2, sum)
        url = 'https://cash.rbc.ru/cash/json/converter_currency_rate/?currency_from=' + value1 + '&currency_to=' + value2 + '&source=cbrf&sum=' + sum + '&date='
        headers = {
            'Cache-Control': 'must-revalidate=False, max-age=3600',
            'Content-Type': 'application/json; charset=utf-8',
            'Date': 'Tue, 17 Jan 2023 19:23:39 GMT',
            'Server': 'QRATOR',
            'Vary': 'User-Agent, Cookie',
            'X-RBC-Conn': 'mrr16:80.68.253.88',
            'X-RBC-GRI': 'P:RI:3fb99529414899909c2f896237001a85'
        }

        response = requests.get(url=url, headers=headers)
        print(response.json()['data']['sum_result'])
        self.ui.output_currency.setText(str(response.json()['data']['sum_result']))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
