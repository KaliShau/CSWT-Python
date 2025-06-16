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

    get_user_by_id = '''
        SELECT * 
        FROM Users 
        WHERE ID = %s;
    '''

    get_users = '''
        SELECT U.ID, U.created_at, U.updated_at, U.username, U.password, U.first_name, U.last_name, U.email, U.phone_number, R.role_name,
        GROUP_CONCAT(d.department_name SEPARATOR ', ') AS departments
        FROM Users U
        JOIN Roles R ON U.role_id = R.ID
        LEFT JOIN User_Departments ud ON U.ID = ud.user_id
        LEFT JOIN Departments d ON ud.department_id = d.id
        GROUP BY U.ID, U.created_at, U.updated_at, U.username, U.password, U.first_name, U.last_name, U.email, U.phone_number, R.role_name;
    '''

    get_users_search = '''
        SELECT U.ID, U.created_at, U.updated_at, U.username, U.password, U.first_name, U.last_name, U.email, U.phone_number, R.role_name,
        GROUP_CONCAT(d.department_name SEPARATOR ', ') AS departments
        FROM Users U
        JOIN Roles R ON U.role_id = R.ID
        LEFT JOIN User_Departments ud ON U.ID = ud.user_id
        LEFT JOIN Departments d ON ud.department_id = d.id
        WHERE U.username LIKE %s OR U.first_name LIKE %s OR U.last_name LIKE %s
        GROUP BY U.ID, U.created_at, U.updated_at, U.username, U.password, U.first_name, U.last_name, U.email, U.phone_number, R.role_name;
    '''

    delete_user = '''
        UPDATE Users
        SET role_id = %s
        WHERE ID = %s;
    '''

    update_user = '''
        UPDATE Users
        SET username = %s, password = %s, first_name = %s, last_name = %s, email = %s, phone_number = %s, role_id = %s
        WHERE ID = %s;
    '''

    delete_role = '''
        DELETE FROM Roles
        WHERE ID = %s;
    '''

    create_role = '''
        INSERT INTO Roles (role_name, description)
        VALUE (%s, %s)
    '''

    get_roles = '''
        SELECT * 
        FROM Roles;
    '''

    get_roles_search = '''
        SELECT * 
        FROM Roles
        WHERE role_name LIKE %s OR description LIKE %s;
    '''

    update_role = '''
        UPDATE Roles
        SET role_name = %s, description = %s
        WHERE ID = %s;
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

    create_priority = '''
        INSERT INTO Priorities (priority_name, description)
        VALUE (%s, %s)
    '''

    get_status_by_name = '''
        SELECT *
        FROM Statuses
        WHERE status_name = %s;
    '''

    get_priorities_search = '''
        SELECT * 
        FROM Priorities
        WHERE priority_name LIKE %s OR description LIKE %s;
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

    get_comment_by_id = '''
        SELECT *
        FROM Comments 
        WHERE ID = %s;
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

    delete_comment = '''
        DELETE FROM Comments
        WHERE ID = %s AND user_id = %s;
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

    closed_at_ticket = '''
        UPDATE Tickets
        SET closed_at = NOW()
        WHERE ID = %s;
    '''

    get_departments_by_user_id = '''
        SELECT d.ID, d.created_at, d.updated_at, d.department_name, d.description
        FROM User_Departments ud
        INNER JOIN Departments d ON ud.department_id = d.id
        WHERE ud.user_id = %s;
    '''

    create_department = '''
        INSERT INTO Departments (department_name, description)
        VALUE (%s, %s) 
    '''

    get_departments_search = '''
        SELECT * 
        FROM Departments
        WHERE department_name LIKE %s OR description LIKE %s;
    '''

    get_departments = '''
        SELECT *
        FROM Departments;
    '''

    get_department_by_name = '''
        SELECT *
        FROM Departments
        WHERE department_name = %s;
    '''

    get_department_by_id = '''
        SELECT *
        FROM Departments
        WHERE ID = %s;
    '''

    update_department = '''
        UPDATE Departments
        SET department_name = %s, description = %s
        WHERE ID = %s;
    '''

    get_departments_not_in_user = '''
        SELECT d.id, d.department_name
        FROM Departments d
            WHERE d.id NOT IN (
            SELECT ud.department_id
            FROM User_Departments ud
            WHERE ud.user_id = %s
        );
    '''

    add_department = '''
        INSERT INTO User_Departments (user_id, department_id)
        VALUE (%s, %s)
    '''

    delete_department = '''
        DELETE FROM Departments 
        WHERE ID = %s;
    '''

    delete_user_department = '''
        DELETE FROM User_Departments 
        WHERE user_id = %s AND department_id = %s;
    '''