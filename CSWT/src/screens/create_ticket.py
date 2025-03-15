from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_CreateTicket(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_CreateTicket, self).__init__()
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
        self.title = QtWidgets.QLabel(parent=self.layout)
        self.title.setGeometry(QtCore.QRect(40, 30, 271, 41))
        font = QtGui.QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.info = QtWidgets.QLabel(parent=self.layout)
        self.info.setGeometry(QtCore.QRect(40, 70, 231, 51))
        font = QtGui.QFont()
        font.setBold(False)
        self.info.setFont(font)
        self.info.setStyleSheet("color: #a5a7aa;")
        self.info.setWordWrap(True)
        self.info.setObjectName("info")
        self.titleLabel = QtWidgets.QLabel(parent=self.layout)
        self.titleLabel.setGeometry(QtCore.QRect(260, 150, 111, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: #a5a7aa;")
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.titleEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.titleEdit.setGeometry(QtCore.QRect(260, 180, 561, 31))
        self.titleEdit.setStyleSheet("")
        self.titleEdit.setObjectName("titleEdit")
        self.priorityComboBox = QtWidgets.QComboBox(parent=self.layout)
        self.priorityComboBox.setGeometry(QtCore.QRect(360, 470, 461, 28))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 33, 34))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.priorityComboBox.setPalette(palette)
        self.priorityComboBox.setObjectName("priorityComboBox")
        self.descLabel = QtWidgets.QLabel(parent=self.layout)
        self.descLabel.setGeometry(QtCore.QRect(260, 240, 111, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.descLabel.setFont(font)
        self.descLabel.setStyleSheet("color: #a5a7aa;")
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName("descLabel")
        self.descEdit = QtWidgets.QTextEdit(parent=self.layout)
        self.descEdit.setGeometry(QtCore.QRect(260, 270, 561, 171))
        self.descEdit.setStyleSheet("")
        self.descEdit.setObjectName("descEdit")
        self.priorityLabel = QtWidgets.QLabel(parent=self.layout)
        self.priorityLabel.setGeometry(QtCore.QRect(260, 460, 91, 41))
        font = QtGui.QFont()
        font.setBold(False)
        self.priorityLabel.setFont(font)
        self.priorityLabel.setStyleSheet("color: #a5a7aa;")
        self.priorityLabel.setWordWrap(True)
        self.priorityLabel.setObjectName("priorityLabel")
        self.addButton = QtWidgets.QCommandLinkButton(parent=self.layout)
        self.addButton.setGeometry(QtCore.QRect(470, 560, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addButton.setFont(font)
        self.addButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.addButton.setDescription("")
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.title.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Добавить заявку</span></p><p><br/></p></body></html>"))
        self.info.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.info.setText(_translate("Form", "<html><head/><body><p>Пожалуйста введить данные</p></body></html>"))
        self.titleLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.titleLabel.setText(_translate("Form", "<html><head/><body><p>Заголовок</p></body></html>"))
        self.descLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.descLabel.setText(_translate("Form", "<html><head/><body><p>Описание</p><p><br/></p></body></html>"))
        self.priorityLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.priorityLabel.setText(_translate("Form", "<html><head/><body><p>Приоритет</p></body></html>"))
        self.addButton.setText(_translate("Form", "Добавить"))

