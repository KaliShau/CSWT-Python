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

    find_by_username = '''
        SELECT * 
        FROM Users 
        WHERE username = %s;
    '''