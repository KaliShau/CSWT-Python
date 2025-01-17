import logging
import mysql.connector

from src.functions.config import config
from src.functions.dialog import dialog

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
                dialog.show(f'Ошибка подключения к базе данных: {err}')

                self.conn = None
                
                return False

    def check_connection(self):
        try:
            config_data = config().load_config()

            conn = mysql.connector.connect(
                host = config_data['database']['host'],
                port = config_data['database']['port'],
                user = config_data['database']['user'] ,
                password = config_data['database']['password'],
                database = config_data['database']['dbname'],
                charset="utf8mb4",
                collation="utf8mb4_unicode_ci"

            )

            if conn.is_connected():
                dialog.show('Успешное подключение')

                conn.close()

                return True

        except mysql.connector.Error as err:
                dialog.show(f'Ошибка подключения: {err}')

                return False

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None
            logging.info('Подключение закрыто')

    def get_user_by_username(self, username):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_user_by_username, username)

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False

    def get_user_by_id(self, id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_user_by_id, (id,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False
        
    def sign_up(self, username, firstname, lastname, number, password, role_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                user_data = (username, firstname, lastname, number, password, role_id)

                cursor.execute(sql.sign_up, user_data)
                self.conn.commit()

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False        
    
    def sign_in(self, username, password):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                user_data = (username, password)

                cursor.execute(sql.sign_in, user_data)
                
                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False        

    def delete_user(self, user_id, role_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.delete_user, (role_id, user_id))
                self.conn.commit()

                dialog.show('Успешно удалено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def delete_role(self, role_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.delete_role, (role_id,))
                self.conn.commit()

                dialog.show('Успешно удалено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def create_role(self, title, desc):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.create_role, (title, desc))
                self.conn.commit()

                dialog.show('Роль успешно добавлена.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def get_role_by_id(self, id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_role_by_id, (id,))
                
                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False      

    def update_role(self, title, desc, role_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.update_role, (title, desc, role_id))
                self.conn.commit()            

                dialog.show('Успешно обновлено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_roles(self):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_roles)
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False      

    def get_roles_search(self, search_term):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_roles_search, ('%' + search_term + '%', '%' + search_term + '%'))

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def get_role_by_name(self, name):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_role_by_name, (name,))
                
                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False      

    def get_my_create_tickets(self, client_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_my_create_tickets, (client_id,))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False      
    
    def get_my_create_tickets_by_title(self, client_id, title):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                search_key = f'%{title}%'

                cursor.execute(sql.get_my_create_tickets_by_title, (client_id, search_key))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False      

    def get_priorities(self):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_priorities)

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def get_priority_by_name(self, name):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_priority_by_name, (name,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False 

    def get_priority_by_id(self, id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_priority_by_id, (id,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def get_status_by_name(self, name):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_status_by_name, (name,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def get_users(self):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_users)

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def get_users_search(self, search_term):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_users_search, ('%' + search_term + '%', '%' + search_term + '%', '%' + search_term + '%'))

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def get_statuses(self):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_statuses)

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_status_by_id(self, id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_status_by_id, (id,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  
    
    def create_ticket(self, title, desc, client_id, priority_id, status_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.create_ticket, (title, desc, client_id, priority_id, status_id))
                self.conn.commit()

                dialog.show('Заявка успешно добавлена.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def delete_ticket_by_client(self, status_id, client_id, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.delete_ticket_by_client, (status_id, client_id, ticket_id))
                self.conn.commit()

                dialog.show('Заявка сменила статус на удалено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def get_ticket_by_id(self, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_ticket_by_id, (ticket_id,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def create_comment(self, text, ticket_id, user_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.create_comment, (text, ticket_id, user_id))
                self.conn.commit()

                dialog.show('Комментарий успешно добавлен.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def get_comments_by_ticket(self, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_comments_by_ticket, (ticket_id,))

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def update_ticket_client(self, title, desc, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.update_ticket_client, (title, desc, ticket_id))
                self.conn.commit()

                dialog.show('Успешно обновлено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def get_available_tickets(self, status_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_available_tickets, (status_id,))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False     

    def get_available_tickets_by_title(self, status_id, title):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                search_key = f'%{title}%'

                cursor.execute(sql.get_available_tickets_by_title, (status_id, search_key))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False      
    
    def update_ticket_by_assigned(self, assigned_to, ticket_id, status_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.update_ticket_by_assigned, (assigned_to, status_id, ticket_id))
                self.conn.commit()

                dialog.show('Успешно добавлено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
    
    def get_my_assigned_tickets(self, user_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_my_assigned_tickets, (user_id,))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_my_assigned_tickets_by_title(self, user_id, title):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                search_key = f'%{title}%'

                cursor.execute(sql.get_my_assigned_tickets_by_title, (user_id, search_key))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def update_ticket(self, title, desc, solution, priority_id, status_id, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.update_ticket, (title, desc, solution, priority_id, status_id, ticket_id))
                self.conn.commit()

                dialog.show('Успешно обновлено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   

    def closed_at_ticket(self, ticket_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.closed_at_ticket, (ticket_id,))
                self.conn.commit()

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False   
                
    def get_departments_by_user_id(self, user_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_departments_by_user_id, (user_id,))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_departments_search(self, search_term):
        if self.conn:
            cursor = self.conn.cursor()
            
            try:
                cursor.execute(sql.get_departments_search, ('%' + search_term + '%', '%' + search_term + '%'))

                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False 

    def get_departments(self):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_departments)
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_department_by_name(self, name):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_department_by_name, (name,))
                
                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_department_by_id(self, id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_department_by_id, (id,))
                
                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def update_department(self, title, desc, department_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.update_department, (title, desc, department_id))
                self.conn.commit()            

                dialog.show('Успешно обновлено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_departments_not_in_user(self, user_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_departments_not_in_user, (user_id,))
                
                result = cursor.fetchall()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def add_department(self, user_id, department_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.add_department, (user_id, department_id))
                self.conn.commit()            

                dialog.show('Отдел добавлен.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def create_department(self, title, desc):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.create_department, (title, desc))
                self.conn.commit()            

                dialog.show('Отдел добавлен.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def delete_department(self, department_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.delete_department, (department_id,))
                self.conn.commit()            

                dialog.show('Отдел удален.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def delete_user_department(self, user_id, department_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.delete_user_department, (user_id, department_id))
                self.conn.commit()            

                dialog.show('Отдел удален.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  
    
    def update_user(self, username, password, firstname, lastname, email, phone_number, role_id, user_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.update_user, (username, password, firstname, lastname, email, phone_number, role_id, user_id))
                self.conn.commit()            

                dialog.show('Успешно обновлено.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  
    
    def delete_comment(self, comment_id, user_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.delete_comment, (comment_id, user_id))
                self.conn.commit()            

                dialog.show('Комментарий удален.')

                return True
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  

    def get_comment_by_id(self, comment_id):
        if self.conn:
            cursor = self.conn.cursor()

            try:
                cursor.execute(sql.get_comment_by_id, (comment_id,))

                result = cursor.fetchone()

                return result
            except mysql.connector.Error as err:
                logging.error('Ошибка при выполнении запроса.')
                dialog.show(f'Ошибка при выполнении запроса: {err}')

                return False  