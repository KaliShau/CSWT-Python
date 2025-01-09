from src.screens.db_config import Ui_DbConfig

from src.functions.config import config

class db_config_functions():
    def __init__(self, main_window, widgets, database_manager):

        # init
        self.db_config = Ui_DbConfig()
        self.main_window = main_window
        self.widgets = widgets
        self.database_manager = database_manager

        # buttons
        self.db_config.saveButton.clicked.connect(self.save_data)
        self.db_config.checkConnectButton.clicked.connect(self.check_connection)
        self.main_window.action.triggered.connect(self.openDbConfig)

    def save_data(self):
        password = self.db_config.passwordEdit.toPlainText()
        user = self.db_config.userEdit.toPlainText()
        host = self.db_config.hostEdit.toPlainText()
        port = self.db_config.portEdit.toPlainText()
        db = self.db_config.dbEdit.toPlainText()

        if not password or not user or not host or not port or not db:
            self.db_config.errorLabel.setVisible(True)
            self.db_config.errorLabel.setText('Поля должны быть заполнены')
            return 
    
        config().save_config(password, user, host, port, db)

        self.db_config.errorLabel.setVisible(True)
        self.db_config.errorLabel.setText('Данные успешно сохранены')

    def check_connection(self):
        self.database_manager.check_connection()
    
    def openDbConfig(self):

        config_data = config().load_config()

        self.db_config.passwordEdit.setPlainText(config_data['database']['password'])
        self.db_config.userEdit.setPlainText(config_data['database']['user'])
        self.db_config.hostEdit.setPlainText(config_data['database']['host'])
        self.db_config.portEdit.setPlainText(config_data['database']['port'])
        self.db_config.dbEdit.setPlainText(config_data['database']['dbname'])

        self.db_config.errorLabel.setVisible(False)

        self.widgets.change(self.db_config)