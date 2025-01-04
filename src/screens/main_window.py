from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 810)
        MainWindow.setStyleSheet("background-color: #1a1a1a;\n"
"color: #e7e7e5")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.centralLayout = QtWidgets.QHBoxLayout()
        self.centralLayout.setObjectName("centralLayout")
        self.navBar = QtWidgets.QWidget(parent=self.centralwidget)
        self.navBar.setMaximumSize(QtCore.QSize(300, 16777215))
        self.navBar.setStyleSheet("QWidget {\n"
"background-color: #202122;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QCommandLinkButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QCommandLinkButton:hover {\n"
"background-color: #dc5049;\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #dc5049;\n"
"\n"
"}")
        self.navBar.setObjectName("navBar")
        self.appName = QtWidgets.QLabel(parent=self.navBar)
        self.appName.setGeometry(QtCore.QRect(10, 10, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.appName.setFont(font)
        self.appName.setObjectName("appName")
        self.line = QtWidgets.QFrame(parent=self.navBar)
        self.line.setGeometry(QtCore.QRect(10, 60, 251, 2))
        self.line.setStyleSheet("background-color: #fff")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.authBox = QtWidgets.QGroupBox(parent=self.navBar)
        self.authBox.setGeometry(QtCore.QRect(10, 90, 281, 121))
        font = QtGui.QFont()
        font.setBold(True)
        self.authBox.setFont(font)
        self.authBox.setObjectName("authBox")
        self.signUpButton = QtWidgets.QCommandLinkButton(parent=self.authBox)
        self.signUpButton.setGeometry(QtCore.QRect(0, 80, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signUpButton.setFont(font)
        self.signUpButton.setDescription("")
        self.signUpButton.setObjectName("signUpButton")
        self.signInButton = QtWidgets.QCommandLinkButton(parent=self.authBox)
        self.signInButton.setGeometry(QtCore.QRect(0, 31, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.signInButton.setFont(font)
        self.signInButton.setDescription("")
        self.signInButton.setObjectName("signInButton")
        self.workBox = QtWidgets.QGroupBox(parent=self.navBar)
        self.workBox.setGeometry(QtCore.QRect(10, 90, 281, 221))
        font = QtGui.QFont()
        font.setBold(True)
        self.workBox.setFont(font)
        self.workBox.setObjectName("workBox")
        self.myTicketsButton = QtWidgets.QCommandLinkButton(parent=self.workBox)
        self.myTicketsButton.setGeometry(QtCore.QRect(0, 80, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myTicketsButton.setFont(font)
        self.myTicketsButton.setDescription("")
        self.myTicketsButton.setObjectName("myTicketsButton")
        self.createTicketButton = QtWidgets.QCommandLinkButton(parent=self.workBox)
        self.createTicketButton.setGeometry(QtCore.QRect(0, 31, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createTicketButton.setFont(font)
        self.createTicketButton.setDescription("")
        self.createTicketButton.setObjectName("createTicketButton")
        self.availableTicketsButton = QtWidgets.QCommandLinkButton(parent=self.workBox)
        self.availableTicketsButton.setGeometry(QtCore.QRect(0, 130, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.availableTicketsButton.setFont(font)
        self.availableTicketsButton.setDescription("")
        self.availableTicketsButton.setObjectName("availableTicketsButton")
        self.myAssignedTicketsButton = QtWidgets.QCommandLinkButton(parent=self.workBox)
        self.myAssignedTicketsButton.setGeometry(QtCore.QRect(0, 180, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myAssignedTicketsButton.setFont(font)
        self.myAssignedTicketsButton.setDescription("")
        self.myAssignedTicketsButton.setObjectName("myAssignedTicketsButton")
        self.reportsBox = QtWidgets.QGroupBox(parent=self.navBar)
        self.reportsBox.setGeometry(QtCore.QRect(10, 320, 281, 171))
        font = QtGui.QFont()
        font.setBold(True)
        self.reportsBox.setFont(font)
        self.reportsBox.setObjectName("reportsBox")
        self.myReportsButton = QtWidgets.QCommandLinkButton(parent=self.reportsBox)
        self.myReportsButton.setGeometry(QtCore.QRect(0, 80, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.myReportsButton.setFont(font)
        self.myReportsButton.setDescription("")
        self.myReportsButton.setObjectName("myReportsButton")
        self.createReportButton = QtWidgets.QCommandLinkButton(parent=self.reportsBox)
        self.createReportButton.setGeometry(QtCore.QRect(0, 31, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.createReportButton.setFont(font)
        self.createReportButton.setDescription("")
        self.createReportButton.setObjectName("createReportButton")
        self.listReportsButton = QtWidgets.QCommandLinkButton(parent=self.reportsBox)
        self.listReportsButton.setGeometry(QtCore.QRect(0, 130, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listReportsButton.setFont(font)
        self.listReportsButton.setDescription("")
        self.listReportsButton.setObjectName("listReportsButton")
        self.adminBox = QtWidgets.QGroupBox(parent=self.navBar)
        self.adminBox.setGeometry(QtCore.QRect(10, 500, 281, 251))
        font = QtGui.QFont()
        font.setBold(True)
        self.adminBox.setFont(font)
        self.adminBox.setObjectName("adminBox")
        self.rolesButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.rolesButton.setGeometry(QtCore.QRect(143, 30, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rolesButton.setFont(font)
        self.rolesButton.setDescription("")
        self.rolesButton.setObjectName("rolesButton")
        self.usersButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.usersButton.setGeometry(QtCore.QRect(0, 31, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usersButton.setFont(font)
        self.usersButton.setDescription("")
        self.usersButton.setObjectName("usersButton")
        self.ticketsButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.ticketsButton.setGeometry(QtCore.QRect(0, 80, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ticketsButton.setFont(font)
        self.ticketsButton.setDescription("")
        self.ticketsButton.setObjectName("ticketsButton")
        self.statusesButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.statusesButton.setGeometry(QtCore.QRect(140, 80, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.statusesButton.setFont(font)
        self.statusesButton.setDescription("")
        self.statusesButton.setObjectName("statusesButton")
        self.prioritiesButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.prioritiesButton.setGeometry(QtCore.QRect(0, 130, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.prioritiesButton.setFont(font)
        self.prioritiesButton.setDescription("")
        self.prioritiesButton.setObjectName("prioritiesButton")
        self.commentsButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.commentsButton.setGeometry(QtCore.QRect(140, 130, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.commentsButton.setFont(font)
        self.commentsButton.setDescription("")
        self.commentsButton.setObjectName("commentsButton")
        self.departamentsButton = QtWidgets.QCommandLinkButton(parent=self.adminBox)
        self.departamentsButton.setGeometry(QtCore.QRect(0, 180, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.departamentsButton.setFont(font)
        self.departamentsButton.setDescription("")
        self.departamentsButton.setObjectName("departamentsButton")
        self.centralLayout.addWidget(self.navBar)
        self.navigationLayout = QtWidgets.QHBoxLayout()
        self.navigationLayout.setObjectName("navigationLayout")
        self.startWidgetLayout = QtWidgets.QWidget(parent=self.centralwidget)
        self.startWidgetLayout.setObjectName("startWidgetLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.startWidgetLayout)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startWidget = QtWidgets.QWidget(parent=self.startWidgetLayout)
        self.startWidget.setMaximumSize(QtCore.QSize(1114, 16777215))
        self.startWidget.setStyleSheet("QWidget {\n"
"background-color: #202122;}")
        self.startWidget.setObjectName("startWidget")
        self.appName_2 = QtWidgets.QLabel(parent=self.startWidget)
        self.appName_2.setGeometry(QtCore.QRect(20, 10, 491, 71))
        font = QtGui.QFont()
        font.setBold(False)
        self.appName_2.setFont(font)
        self.appName_2.setStyleSheet("color: #a5a7aa;")
        self.appName_2.setWordWrap(True)
        self.appName_2.setObjectName("appName_2")
        self.horizontalLayout.addWidget(self.startWidget)
        self.navigationLayout.addWidget(self.startWidgetLayout)
        self.centralLayout.addLayout(self.navigationLayout)
        self.horizontalLayout_2.addLayout(self.centralLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1440, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
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
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
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
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 26, 26))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(231, 231, 229, 128))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.menubar.setPalette(palette)
        self.menubar.setStyleSheet("border-bottom: 2px solid #202122")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appName.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.appName.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">CSWT</span></p></body></html>"))
        self.authBox.setTitle(_translate("MainWindow", "Авторизация  "))
        self.signUpButton.setText(_translate("MainWindow", "Регистрация"))
        self.signInButton.setText(_translate("MainWindow", "Вход"))
        self.workBox.setTitle(_translate("MainWindow", "Работа"))
        self.myTicketsButton.setText(_translate("MainWindow", "Мои заявки"))
        self.createTicketButton.setText(_translate("MainWindow", "Создать заявку"))
        self.availableTicketsButton.setText(_translate("MainWindow", "Список заявок"))
        self.myAssignedTicketsButton.setText(_translate("MainWindow", "Мои принятые заявки"))
        self.reportsBox.setTitle(_translate("MainWindow", "Отчеты"))
        self.myReportsButton.setText(_translate("MainWindow", "Мои отчеты"))
        self.createReportButton.setText(_translate("MainWindow", "Создать отчет"))
        self.listReportsButton.setText(_translate("MainWindow", "Список отчетов"))
        self.adminBox.setTitle(_translate("MainWindow", "Администрирование"))
        self.rolesButton.setText(_translate("MainWindow", "Роли"))
        self.usersButton.setText(_translate("MainWindow", "Пользовате.."))
        self.ticketsButton.setText(_translate("MainWindow", "Заявки"))
        self.statusesButton.setText(_translate("MainWindow", "Статусы"))
        self.prioritiesButton.setText(_translate("MainWindow", "Приоритеты"))
        self.commentsButton.setText(_translate("MainWindow", "Комментар..."))
        self.departamentsButton.setText(_translate("MainWindow", "Отделы"))
        self.appName_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:400;\">Control System Work Tracker</span></p></body></html>"))
        self.appName_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Для получения доступа к функционалу системы нужно зарегистрироваться или войти в систему!</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "Профиль"))
        self.menu_2.setTitle(_translate("MainWindow", "Настройки"))
        self.action.setText(_translate("MainWindow", "База данных"))
        self.action_2.setText(_translate("MainWindow", "Изменить"))
        self.action_3.setText(_translate("MainWindow", "Статистика"))
        self.action_5.setText(_translate("MainWindow", "Выйти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
