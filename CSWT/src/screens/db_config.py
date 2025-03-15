from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DbConfig(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_DbConfig, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1112, 763)
        self.setStyleSheet("background-color: #1a1a1a;\n"
"color: #e7e7e5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout = QtWidgets.QWidget(parent=self)
        self.layout.setMaximumSize(QtCore.QSize(1094, 16777215))
        self.layout.setStyleSheet("QWidget {\n"
"background-color: #202122;\n"
"}\n"
"\n"
"QTextEdit {\n"
"border: 1px solid #353738;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"border: 1px solid #dc5049;\n"
"}\n"
"\n"
"")
        self.layout.setObjectName("layout")
        self.errorLabel = QtWidgets.QLabel(parent=self.layout)
        self.errorLabel.setGeometry(QtCore.QRect(730, 320, 301, 81))
        font = QtGui.QFont()
        font.setBold(False)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: #a5a7aa;")
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.hostLabel = QtWidgets.QLabel(parent=self.layout)
        self.hostLabel.setGeometry(QtCore.QRect(730, 70, 61, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.hostLabel.setFont(font)
        self.hostLabel.setStyleSheet("color: #a5a7aa;")
        self.hostLabel.setWordWrap(True)
        self.hostLabel.setObjectName("hostLabel")
        self.hostEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.hostEdit.setGeometry(QtCore.QRect(730, 90, 301, 31))
        self.hostEdit.setStyleSheet("")
        self.hostEdit.setObjectName("hostEdit")
        self.saveButton = QtWidgets.QCommandLinkButton(parent=self.layout)
        self.saveButton.setGeometry(QtCore.QRect(390, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveButton.setFont(font)
        self.saveButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.saveButton.setDescription("")
        self.saveButton.setObjectName("saveButton")
        self.title = QtWidgets.QLabel(parent=self.layout)
        self.title.setGeometry(QtCore.QRect(50, 20, 211, 91))
        font = QtGui.QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.portLabel = QtWidgets.QLabel(parent=self.layout)
        self.portLabel.setGeometry(QtCore.QRect(730, 160, 61, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.portLabel.setFont(font)
        self.portLabel.setStyleSheet("color: #a5a7aa;")
        self.portLabel.setWordWrap(True)
        self.portLabel.setObjectName("portLabel")
        self.portEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.portEdit.setGeometry(QtCore.QRect(730, 180, 301, 31))
        self.portEdit.setStyleSheet("")
        self.portEdit.setObjectName("portEdit")
        self.userLabel = QtWidgets.QLabel(parent=self.layout)
        self.userLabel.setGeometry(QtCore.QRect(390, 160, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("color: #a5a7aa;")
        self.userLabel.setWordWrap(True)
        self.userLabel.setObjectName("userLabel")
        self.userEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.userEdit.setGeometry(QtCore.QRect(390, 180, 301, 31))
        self.userEdit.setStyleSheet("")
        self.userEdit.setObjectName("userEdit")
        self.passwordLabel = QtWidgets.QLabel(parent=self.layout)
        self.passwordLabel.setGeometry(QtCore.QRect(390, 70, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color: #a5a7aa;")
        self.passwordLabel.setWordWrap(True)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.passwordEdit.setGeometry(QtCore.QRect(390, 90, 301, 31))
        self.passwordEdit.setStyleSheet("")
        self.passwordEdit.setObjectName("passwordEdit")
        self.dbLabel = QtWidgets.QLabel(parent=self.layout)
        self.dbLabel.setGeometry(QtCore.QRect(730, 250, 91, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.dbLabel.setFont(font)
        self.dbLabel.setStyleSheet("color: #a5a7aa;")
        self.dbLabel.setWordWrap(True)
        self.dbLabel.setObjectName("dbLabel")
        self.dbEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.dbEdit.setGeometry(QtCore.QRect(730, 270, 301, 31))
        self.dbEdit.setStyleSheet("")
        self.dbEdit.setObjectName("dbEdit")
        self.checkConnectButton = QtWidgets.QCommandLinkButton(parent=self.layout)
        self.checkConnectButton.setGeometry(QtCore.QRect(30, 110, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkConnectButton.setFont(font)
        self.checkConnectButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.checkConnectButton.setDescription("")
        self.checkConnectButton.setObjectName("checkConnectButton")
        self.horizontalLayout.addWidget(self.layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.errorLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.errorLabel.setText(_translate("Form", "<html><head/><body><p>Ошибка</p></body></html>"))
        self.hostLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.hostLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Хост</span></p><p><br/></p></body></html>"))
        self.saveButton.setText(_translate("Form", "Сохранить"))
        self.title.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Настройка базы данных</span></p></body></html>"))
        self.portLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.portLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Порт</span></p></body></html>"))
        self.userLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.userLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Пользователь</span></p></body></html>"))
        self.passwordLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.passwordLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">Пароль</span></p></body></html>"))
        self.dbLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.dbLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:10pt;\">База данных</span></p></body></html>"))
        self.checkConnectButton.setText(_translate("Form", "Проверить подключение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
