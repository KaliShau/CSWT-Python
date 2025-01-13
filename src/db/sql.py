class sql():
    sign_up = '''
        INSERT INTO Users (username, first_name, last_name, phone_number, password, role_id)
        VALUES (%s, %s, %s, %s, %s, %s);
    '''

    sign_in = '''
        SELECT * 
        FROM Users 
        WHERE username = %s AND password = %s;
    '''

    get_user_by_username = '''
        SELECT * 
        FROM Users 
        WHERE username = %s;
    '''

    get_role_by_id = '''
        SELECT * 
        FROM Roles 
        WHERE ID = %s;
    '''
    
    get_role_by_name = '''
        SELECT * 
        FROM Roles 
        WHERE role_name = %s;
    '''

    get_my_create_tickets = '''
        SELECT T.ID, T.created_at, T.title, T.description, T.solution, T.closed_at, P.priority_name, S.status_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.first_name ELSE NULL END AS assigned_first_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.last_name ELSE NULL END AS assigned_last_name   
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        LEFT JOIN Users U ON T.assigned_to = U.ID
        WHERE T.client_id = %s 
        ORDER BY T.created_at DESC;
    '''

    get_my_create_tickets_by_title = '''
        SELECT T.ID, T.created_at, T.title, T.description, T.solution, T.closed_at, P.priority_name, S.status_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.first_name ELSE NULL END AS assigned_first_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.last_name ELSE NULL END AS assigned_last_name   
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        LEFT JOIN Users U ON T.assigned_to = U.ID
        WHERE T.client_id = %s AND T.title LIKE %s 
        ORDER BY T.created_at DESC;
    '''

    get_available_tickets = '''
        SELECT T.ID, T.created_at, T.title, T.description, P.priority_name, S.status_name, U.first_name, U.last_name
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        JOIN Users U ON T.client_id = U.ID
        WHERE T.status_id = %s
        ORDER BY T.created_at DESC;
    '''

    get_available_tickets_by_title = '''
        SELECT T.ID, T.created_at, T.title, T.description, P.priority_name, S.status_name, U.first_name, U.last_name
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        JOIN Users U ON T.client_id = U.ID
        WHERE T.status_id = %s AND T.title LIKE %s 
        ORDER BY T.created_at DESC;
    '''

    get_priorities = '''
        SELECT * 
        FROM Priorities;
    '''

    get_priority_by_name = '''
        SELECT *
        FROM Priorities
        WHERE priority_name = %s;
    '''

    get_priority_by_id = '''
        SELECT *
        FROM Priorities
        WHERE ID = %s;
    '''

    get_status_by_name = '''
        SELECT *
        FROM Statuses
        WHERE status_name = %s;
    '''

    get_statuses = '''
        SELECT *
        FROM Statuses;
    '''

    get_status_by_id = '''
        SELECT *
        FROM Statuses
        WHERE ID = %s;
    '''

    create_ticket = '''
        INSERT INTO Tickets (title, description, client_id, priority_id, status_id)
        VALUE (%s, %s, %s, %s, %s)
    '''

    delete_ticket_by_client = '''
        UPDATE Tickets
        SET status_id = %s
        WHERE client_id = %s AND ID = %s;
    '''

    get_comments_by_ticket = '''
        SELECT C.ID, C.created_at, C.comment_text, U.first_name, U.last_name
        FROM Comments C
        JOIN Users U ON C.user_id = U.ID
        WHERE ticket_id = %s;
    '''

    get_ticket_by_id = '''
        SELECT *
        FROM Tickets
        WHERE ID = %s;
    '''

    create_comment = '''
        INSERT INTO Comments (comment_text, ticket_id, user_id)
        VALUE (%s, %s, %s) 
    '''

    update_ticket_client = '''
        UPDATE Tickets
        SET title = %s, description = %s
        WHERE ID = %s;
    '''

    update_ticket_by_assigned = '''
        UPDATE Tickets
        SET assigned_to = %s, status_id = %s
        WHERE ID = %s;
    '''

    get_my_assigned_tickets = '''
        SELECT T.ID, T.created_at, T.title, T.description, T.solution, T.closed_at, P.priority_name, S.status_name, U.first_name, U.last_name
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        JOIN Users U ON T.client_id = U.ID
        WHERE T.assigned_to = %s
        ORDER BY T.created_at DESC;
    '''

    get_my_assigned_tickets_by_title = '''
        SELECT T.ID, T.created_at, T.title, T.description, T.solution, T.closed_at, P.priority_name, S.status_name, U.first_name, U.last_name
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        JOIN Users U ON T.client_id = U.ID
        WHERE T.assigned_to = %s AND T.title LIKE %s
        ORDER BY T.created_at DESC;
    '''

    update_ticket = '''
        UPDATE Tickets
        SET title = %s, description = %s, solution = %s, priority_id = %s, status_id = %s
        WHERE ID = %s;
    '''

    create_base_roles = '''
        INSERT INTO Roles (role_name, description)
        VALUE 
            ('Client', 'Клиент, создающий заявки и отслеживающий их.'),
            ('Admin', 'Администратор системы, управляющий пользователями и системой'),
            ('ASU_staff', 'Сотрудник АСУ, работающий с заявками и помогающий клиентам.');
    '''

    create_base_statuses = '''
        INSERT INTO Priorities (priority_name, description)
        VALUE 
            ('Низкий', 'Заявка может быть отложена на длительное время, не срочная.'),
            ('Нормальный', ' Заявка требует внимания, но не является срочной.'),
            ('Средний', 'Заявка требует более быстрого решения.'),
            ('Высокий', ' Заявка требует срочного решения.'),
            ('Критический', ' Заявка требует немедленного решения.');
    '''

    closed_at_ticket = '''
        UPDATE Tickets
        SET closed_at = NOW()
        WHERE ID = %s;
    '''