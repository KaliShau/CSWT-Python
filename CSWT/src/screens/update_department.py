from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_UpdateDepartment(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_UpdateDepartment, self).__init__()
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
"QComboBox {\n"
"border: 1px solid #353738;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"border: 1px solid #dc5049;\n"
"}")
        self.layout.setObjectName("layout")
        self.topBar = QtWidgets.QWidget(parent=self.layout)
        self.topBar.setGeometry(QtCore.QRect(20, 10, 1094, 721))
        self.topBar.setMinimumSize(QtCore.QSize(0, 200))
        self.topBar.setObjectName("topBar")
        self.title = QtWidgets.QLabel(parent=self.topBar)
        self.title.setGeometry(QtCore.QRect(30, 20, 231, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.updateTicketButton = QtWidgets.QCommandLinkButton(parent=self.topBar)
        self.updateTicketButton.setGeometry(QtCore.QRect(440, 460, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.updateTicketButton.setFont(font)
        self.updateTicketButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.updateTicketButton.setDescription("")
        self.updateTicketButton.setObjectName("updateTicketButton")
        self.titleLabel = QtWidgets.QLabel(parent=self.topBar)
        self.titleLabel.setGeometry(QtCore.QRect(240, 110, 111, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: #a5a7aa;")
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.descEdit = QtWidgets.QTextEdit(parent=self.topBar)
        self.descEdit.setGeometry(QtCore.QRect(240, 230, 561, 171))
        self.descEdit.setStyleSheet("")
        self.descEdit.setObjectName("descEdit")
        self.titleEdit = QtWidgets.QTextEdit(parent=self.topBar)
        self.titleEdit.setGeometry(QtCore.QRect(240, 140, 561, 31))
        self.titleEdit.setStyleSheet("")
        self.titleEdit.setObjectName("titleEdit")
        self.descLabel = QtWidgets.QLabel(parent=self.topBar)
        self.descLabel.setGeometry(QtCore.QRect(240, 200, 111, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.descLabel.setFont(font)
        self.descLabel.setStyleSheet("color: #a5a7aa;")
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName("descLabel")
        self.horizontalLayout.addWidget(self.layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.title.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Отдел:</span></p></body></html>"))
        self.updateTicketButton.setText(_translate("Form", "Сохранить"))
        self.titleLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.titleLabel.setText(_translate("Form", "<html><head/><body><p>Название</p><p><br/></p></body></html>"))
        self.descLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.descLabel.setText(_translate("Form", "<html><head/><body><p>Описание</p><p><br/></p></body></html>"))
