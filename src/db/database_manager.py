import logging
import mysql.connector

from src.functions.config import config

from src.screens.dialog import Ui_Dialog

from src.db.sql_tables import sql_tables
from src.db.sql import sql 

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class database_manager():
    def __init__(self):

        self.conn = None

    def connect(self):
        if not self.conn:
            try:
                logging.info('Попытка подключения к базе данных...')

                config_data = config().load_config()

                self.conn = mysql.connector.connect(
                    host = config_data['database']['host'],
                    port = config_data['database']['port'],
                    user = config_data['database']['user'] ,
                    password = config_data['database']['password'],
                    database = config_data['database']['dbname'],
                    charset="utf8mb4",
                    collation="utf8mb4_unicode_ci"
                )

                logging.info('Успешное подключение к базе данных.')
                logging.info('Проверка таблиц...')

                cursor = self.conn.cursor()

                cursor.execute(sql_tables.roles)
                cursor.execute(sql_tables.statuses)
                cursor.execute(sql_tables.priorities)
                cursor.execute(sql_tables.departments)
                cursor.execute(sql_tables.users)
                cursor.execute(sql_tables.tickets)
                cursor.execute(sql_tables.comments)
                cursor.execute(sql_tables.user_departments)
                cursor.execute(sql_tables.reports)

                self.conn.commit()

                logging.info('Таблицы исправны.')

                return True

            except mysql.connector.Error as err:
                logging.error(f'Ошибка подключения к базе данных: {err}')
                
                self.conn = None
                
                return False

    def check_connection(self):
        try:
            config_data = config().load_config()

            self.conn = mysql.connector.connect(
                host = config_data['database']['host'],
                port = config_data['database']['port'],
                user = config_data['database']['user'] ,
                password = config_data['database']['password'],
                database = config_data['database']['dbname'],
                charset="utf8mb4",
                collation="utf8mb4_unicode_ci"

            )

            if self.conn.is_connected():
                dialog = Ui_Dialog()
                dialog.textLabel.setText(f'Успешное подключение')
                dialog.show()
                dialog.exec()
                self.conn.close()

                return True

        except mysql.connector.Error as err:
                dialog = Ui_Dialog()
                dialog.textLabel.setText(f'Ошибка подключения: {err}')
                dialog.show()
                dialog.exec()

                return False

    def find_by_username(self, username):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.find_by_username, username)

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog = Ui_Dialog()
                dialog.textLabel.setText(f'Ошибка при выполнении запроса: {err}')
                dialog.show()
                dialog.exec()

                return False

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            logging.info('Подключение закрыто')
        
    def sign_up(self, username, firstname, lastname, number, password):
        cursor = self.conn.cursor()

        try:
            user_data = (username, firstname, lastname, number, password)

            cursor.execute(sql.sign_up, user_data)
            self.conn.commit()

            return True
        except mysql.connector.Error as err:
            logging.error('Ошибка при выполнении запроса.')
            dialog = Ui_Dialog()
            dialog.textLabel.setText(f'Ошибка при выполнении запроса: {err}')
            dialog.show()
            dialog.exec()

            return False        
    
    def sign_in(self, username, password):
        cursor = self.conn.cursor()

        try:
            user_data = (username, password)

            cursor.execute(sql.sign_in, user_data)
            
            result = cursor.fetchone()

            return result
        except mysql.connector.Error as err:
            logging.error('Ошибка при выполнении запроса.')
            dialog = Ui_Dialog()
            dialog.textLabel.setText(f'Ошибка при выполнении запроса: {err}')
            dialog.show()
            dialog.exec()

            return False        