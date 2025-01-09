from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setupUi()

        self.okButton.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.close()

    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(500, 200)
        self.setStyleSheet("background-color: #1a1a1a;\n"
"color: #e7e7e5;")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=self)
        self.widget.setMaximumSize(QtCore.QSize(500, 200))
        self.widget.setObjectName("widget")
        self.okButton = QtWidgets.QPushButton(parent=self.widget)
        self.okButton.setGeometry(QtCore.QRect(0, 150, 480, 31))
        self.okButton.setStyleSheet("QPushButton {\n"
"border: 2px solid #202122;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #dc5049\n"
"}")
        self.okButton.setObjectName("okButton")
        self.title = QtWidgets.QLabel(parent=self.widget)
        self.title.setGeometry(QtCore.QRect(30, 10, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.line = QtWidgets.QFrame(parent=self.widget)
        self.line.setGeometry(QtCore.QRect(0, 50, 480, 2))
        self.line.setStyleSheet("background-color: #353738\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.textLabel = QtWidgets.QLabel(parent=self.widget)
        self.textLabel.setGeometry(QtCore.QRect(10, 60, 461, 71))
        font = QtGui.QFont()
        font.setBold(False)
        self.textLabel.setFont(font)
        self.textLabel.setStyleSheet("color: #a5a7aa;")
        self.textLabel.setWordWrap(True)
        self.textLabel.setObjectName("textLabel")
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.okButton.setText(_translate("Dialog", "Ок"))
        self.title.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt;\">Уведомление</span></p></body></html>"))
        self.textLabel.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.textLabel.setText(_translate("Dialog", "<html><head/><body><p>Text</p><p><br/></p></body></html>"))


