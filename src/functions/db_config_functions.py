from src.screens.db_config import Ui_DbConfig
from src.functions.config import config

class db_config_functions():
    def __init__(self, config: config, db_config: Ui_DbConfig):
        self.config = config
        self.db_config = db_config

        self.db_config.saveButton.clicked.connect(self.save_data)

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
    
        self.config.save_config(password, user, host, port, db)

        self.db_config.errorLabel.setVisible(True)
        self.db_config.errorLabel.setText('Данные успешно сохранены')