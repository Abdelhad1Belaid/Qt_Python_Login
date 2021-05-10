from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(337, 450)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setStyleSheet("QPushButton{\n"
"    background-color:rgba(2, 65, 118, 255);\n"
"    color:rgba(255, 255, 255, 200);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(2, 65, 118, 100);\n"
"    background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(2, 65, 118, 200);\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 290, 410))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 290, 410))
        self.label.setStyleSheet("background-color:rgba(16, 30, 41, 240);\n"
"border-radius:10px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 210, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 260, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"color:rgb(255, 255, 255);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 180, 150))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Tamil")
        font.setPointSize(80)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"color:rgba(0, 125, 236, 255);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.exit = QtWidgets.QPushButton(self.widget)
        self.exit.setGeometry(QtCore.QRect(260, 0, 27, 27))
        self.exit.setMaximumSize(QtCore.QSize(27, 27))
        font = QtGui.QFont()
        font.setFamily("Font Awesome 5 Free Regular")
        font.setPointSize(15)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color:transparent;")
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        self.exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  Username"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g i n"))
        self.label_2.setText(_translate("Form", ""))
        self.exit.setText(_translate("Form", ""))
