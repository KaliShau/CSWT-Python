from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Departments(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Departments, self).__init__()
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
        self.tabWidget = QtWidgets.QTabWidget(parent=self.layout)
        self.tabWidget.setGeometry(QtCore.QRect(0, 90, 1091, 661))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_roles = QtWidgets.QWidget()
        self.tab_roles.setObjectName("tab_roles")
        self.tableView = QtWidgets.QTableView(parent=self.tab_roles)
        self.tableView.setGeometry(QtCore.QRect(0, 110, 1090, 521))
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
        self.searchLabel = QtWidgets.QLabel(parent=self.tab_roles)
        self.searchLabel.setGeometry(QtCore.QRect(10, 20, 351, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.searchLabel.setFont(font)
        self.searchLabel.setStyleSheet("color: #a5a7aa;")
        self.searchLabel.setWordWrap(True)
        self.searchLabel.setObjectName("searchLabel")
        self.searchEdit = QtWidgets.QTextEdit(parent=self.tab_roles)
        self.searchEdit.setGeometry(QtCore.QRect(10, 50, 261, 31))
        self.searchEdit.setStyleSheet("")
        self.searchEdit.setObjectName("searchEdit")
        self.searchButton = QtWidgets.QCommandLinkButton(parent=self.tab_roles)
        self.searchButton.setGeometry(QtCore.QRect(290, 40, 121, 41))
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
        self.tabWidget.addTab(self.tab_roles, "")
        self.tab_create_role = QtWidgets.QWidget()
        self.tab_create_role.setObjectName("tab_create_role")
        self.createButton = QtWidgets.QCommandLinkButton(parent=self.tab_create_role)
        self.createButton.setGeometry(QtCore.QRect(480, 450, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"}")
        self.createButton.setDescription("")
        self.createButton.setObjectName("createButton")
        self.descLabel = QtWidgets.QLabel(parent=self.tab_create_role)
        self.descLabel.setGeometry(QtCore.QRect(270, 180, 111, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.descLabel.setFont(font)
        self.descLabel.setStyleSheet("color: #a5a7aa;")
        self.descLabel.setWordWrap(True)
        self.descLabel.setObjectName("descLabel")
        self.titleLabel = QtWidgets.QLabel(parent=self.tab_create_role)
        self.titleLabel.setGeometry(QtCore.QRect(270, 90, 111, 21))
        font = QtGui.QFont()
        font.setBold(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("color: #a5a7aa;")
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.titleEdit = QtWidgets.QTextEdit(parent=self.tab_create_role)
        self.titleEdit.setGeometry(QtCore.QRect(270, 120, 561, 31))
        self.titleEdit.setStyleSheet("")
        self.titleEdit.setObjectName("titleEdit")
        self.descEdit = QtWidgets.QTextEdit(parent=self.tab_create_role)
        self.descEdit.setGeometry(QtCore.QRect(270, 210, 561, 171))
        self.descEdit.setStyleSheet("")
        self.descEdit.setObjectName("descEdit")
        self.tabWidget.addTab(self.tab_create_role, "")
        self.horizontalLayout.addWidget(self.layout)

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.title.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.title.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:24pt;\">Отделы</span></p></body></html>"))
        self.searchLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.searchLabel.setText(_translate("Form", "<html><head/><body><p>Поиск по названию и описанию</p></body></html>"))
        self.searchButton.setText(_translate("Form", "Найти"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_roles), _translate("Form", "Просмотр"))
        self.createButton.setText(_translate("Form", "Добавить"))
        self.descLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.descLabel.setText(_translate("Form", "<html><head/><body><p>Описание</p><p><br/></p></body></html>"))
        self.titleLabel.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.titleLabel.setText(_translate("Form", "<html><head/><body><p>Название</p><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_create_role), _translate("Form", "Добавить"))
