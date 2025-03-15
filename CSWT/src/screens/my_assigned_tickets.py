from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MyAssignedTickets(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_MyAssignedTickets, self).__init__()
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
        self.tableView = QtWidgets.QTableView(parent=self.layout)
        self.tableView.setGeometry(QtCore.QRect(0, 260, 1090, 491))
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
        brush = QtGui.QBrush(QtGui.QColor(220, 80, 73))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Highlight, brush)
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
        brush = QtGui.QBrush(QtGui.QColor(220, 80, 73))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Highlight, brush)
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
        self.tableView.setPalette(palette)
        self.tableView.setStyleSheet("border: 1px solid #353738")
        self.tableView.setObjectName("tableView")
        self.topBar = QtWidgets.QWidget(parent=self.layout)
        self.topBar.setGeometry(QtCore.QRect(9, 9, 1094, 200))
        self.topBar.setMinimumSize(QtCore.QSize(0, 200))
        self.topBar.setObjectName("topBar")
        self.searchLabel = QtWidgets.QLabel(parent=self.topBar)
        self.searchLabel.setGeometry(QtCore.QRect(410, 30, 161, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.searchLabel.setFont(font)
        self.searchLabel.setStyleSheet("color: #a5a7aa;")
        self.searchLabel.setWordWrap(True)
        self.searchLabel.setObjectName("searchLabel")
        self.searchEdit = QtWidgets.QTextEdit(parent=self.topBar)
        self.searchEdit.setGeometry(QtCore.QRect(410, 60, 561, 31))
        self.searchEdit.setStyleSheet("")
        self.searchEdit.setObjectName("searchEdit")
        self.searchButton = QtWidgets.QCommandLinkButton(parent=self.topBar)
        self.searchButton.setGeometry(QtCore.QRect(410, 110, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.searchButton.setFont(font)
        self.searchButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.searchButton.setDescription("")
        self.searchButton.setObjectName("searchButton")
        self.title = QtWidgets.QLabel(parent=self.topBar)
        self.title.setGeometry(QtCore.QRect(30, 20, 271, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.title.setFont(font)
        self.title.setWordWrap(True)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.layout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.searchLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.searchLabel.setText(_translate("Form", "<html><head/><body><p>Поиск по загаловку</p><p><br/></p><p><br/></p></body></html>"))
        self.searchButton.setText(_translate("Form", "Найти"))
        self.title.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Мои принятые заявки</span></p></body></html>"))

