from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:#22222e\n"
                                         "")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 651, 271))
        self.frame.setStyleSheet("background-color: #483D8B")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 10, 311, 111))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(300, 110, 241, 121))
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap("C:/Users/letin/OneDrive/Рабочий стол/icons8-получить-доллары-наличными-64.png"))
        self.label_2.setObjectName("label_2")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(60, 360, 341, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background-color:#22222e;\n"
                                        "border:2px solid#483D8B;\n"
                                        "border-radius:30;\n"
                                        "color:white;")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(60, 540, 340, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color:#22222e;\n"
                                           "border:2px solid#483D8B;\n"
                                           "border-radius:30;\n"
                                           "color:white;")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(64, 632, 331, 61))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    background-color:#483D8B;\n"
                                      "    border:2px solid#483D8B;\n"
                                      "    border-radius:30;\n"
                                      "    color:white;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed{\n"
                                      "    background-color:#683F8B\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(68, 281, 321, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:#22222e;\n"
                                    "border:2px solid#483D8B;\n"
                                    "border-radius:30;\n"
                                    "color:white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 450, 321, 51))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("background-color:#22222e;\n"
                                      "border:2px solid#483D8B;\n"
                                      "border-radius:30;\n"
                                      "color:white;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 280, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 330, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 330, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(590, 330, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(490, 380, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 380, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "    background-color:#22222e;\n"
                                        "    border:2px solid#483D8B;\n"
                                        "    border-radius:30;\n"
                                        "    color:white;\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#683F8B\n"
                                        "}\n"
                                        "")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(590, 380, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("QPushButton{\n"
                                         "    background-color:#22222e;\n"
                                         "    border:2px solid#483D8B;\n"
                                         "    border-radius:30;\n"
                                         "    color:white;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color:#683F8B\n"
                                         "}\n"
                                         "")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(540, 430, 50, 50))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("QPushButton{\n"
                                         "    background-color:#22222e;\n"
                                         "    border:2px solid#483D8B;\n"
                                         "    border-radius:30;\n"
                                         "    color:white;\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "    background-color:#683F8B\n"
                                         "}\n"
                                         "")
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "КОНВЕРТЕР ВАЛЮТ"))
        self.input_amount.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРУЙ"))
        self.comboBox.setItemText(0, _translate("MainWindow", "EUR"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RUR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "GPB"))
        self.comboBox.setItemText(3, _translate("MainWindow", "USD"))
        self.comboBox.setItemText(4, _translate("MainWindow", "BYN"))
        self.comboBox.setItemText(5, _translate("MainWindow", "CAD"))
        self.comboBox.setItemText(6, _translate("MainWindow", "AMD"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "EUR"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "RUR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "GBP"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "USD"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "BYN"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "CAD"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "AMD"))
        self.pushButton_2.setText(_translate("MainWindow", "7"))
        self.pushButton_3.setText(_translate("MainWindow", "8"))
        self.pushButton_4.setText(_translate("MainWindow", "9"))
        self.pushButton_5.setText(_translate("MainWindow", "4"))
        self.pushButton_6.setText(_translate("MainWindow", "5"))
        self.pushButton_7.setText(_translate("MainWindow", "6"))
        self.pushButton_8.setText(_translate("MainWindow", "1"))
        self.pushButton_9.setText(_translate("MainWindow", "2"))
        self.pushButton_10.setText(_translate("MainWindow", "3"))
        self.pushButton_11.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
