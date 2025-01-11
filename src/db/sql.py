class sql():
    sign_up = '''
        INSERT INTO Users (username, first_name, last_name, phone_number, password, role_id)
        VALUES (%s, %s, %s, %s, %s, 3);
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
    
    get_my_create_tickets = '''
        SELECT T.ID, T.created_at, T.title, T.description, T.solution, T.closed_at, P.priority_name, S.status_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.first_name ELSE NULL END AS assigned_first_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.last_name ELSE NULL END AS assigned_last_name   
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        LEFT JOIN Users U ON T.assigned_to = U.ID
        WHERE T.client_id = %s;
    '''

    get_my_create_tickets_by_title = '''
        SELECT T.ID, T.created_at, T.title, T.description, T.solution, T.closed_at, P.priority_name, S.status_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.first_name ELSE NULL END AS assigned_first_name,
        CASE WHEN T.assigned_to IS NOT NULL THEN U.last_name ELSE NULL END AS assigned_last_name   
        FROM Tickets T
        JOIN Statuses S ON T.status_id = S.ID
        JOIN Priorities P ON T.priority_id = P.ID
        LEFT JOIN Users U ON T.assigned_to = U.ID
        WHERE T.client_id = %s AND T.title LIKE %s;
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

    get_status_by_name = '''
        SELECT *
        FROM Statuses
        WHERE status_name = %s;
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