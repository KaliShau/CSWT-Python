class sql_tables():

    # create tables
    roles = '''
        CREATE TABLE IF NOT EXISTS Roles (

        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        role_name VARCHAR(50) NOT NULL UNIQUE,
        description TEXT
        )
    '''

    statuses = '''
        CREATE TABLE IF NOT EXISTS Statuses (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        status_name VARCHAR(50) NOT NULL UNIQUE,
        description TEXT
        )
    '''

    priorities = '''
        CREATE TABLE IF NOT EXISTS Priorities (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        priority_name VARCHAR(50) NOT NULL UNIQUE,
        description TEXT
        )
    '''    

    departments = '''
        CREATE TABLE IF NOT EXISTS Departments (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        department_name VARCHAR(50) NOT NULL UNIQUE,
        description TEXT
        )
    '''    

    users = '''
        CREATE TABLE IF NOT EXISTS Users (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        username VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL,

        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100) UNIQUE,
        phone_number VARCHAR(20),

        role_id INT NOT NULL,

        FOREIGN KEY (role_id) REFERENCES Roles(ID)
        )
    '''

    tickets = '''
        CREATE TABLE IF NOT EXISTS Tickets (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        title TEXT NOT NULL,
        description TEXT NOT NULL,
        solution TEXT,

        closed_at TIMESTAMP,

        client_id INT NOT NULL,
        priority_id INT NOT NULL,
        status_id INT NOT NULL,
        assigned_to INT,

        FOREIGN KEY (client_id) REFERENCES Users(ID),
        FOREIGN KEY (priority_id) REFERENCES Priorities(ID),
        FOREIGN KEY (status_id) REFERENCES Statuses(ID),
        FOREIGN KEY (assigned_to) REFERENCES Users(ID)
        )
    '''

    comments = '''
        CREATE TABLE IF NOT EXISTS Comments (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        comment_text TEXT NOT NULL,

        ticket_id INT NOT NULL,
        user_id INT NOT NULL,

        FOREIGN KEY (ticket_id) REFERENCES Tickets(ID),
        FOREIGN KEY (user_id) REFERENCES Users(ID)
        )
    '''

    user_departments = '''
        CREATE TABLE IF NOT EXISTS User_Departments (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        user_id INT NOT NULL,
        department_id INT NOT NULL,

        FOREIGN KEY (user_id) REFERENCES Users(ID),
        FOREIGN KEY (department_id) REFERENCES Departments(ID)
        )
    '''

    reports = '''
        CREATE TABLE IF NOT EXISTS Reports (
        
        ID INT PRIMARY KEY AUTO_INCREMENT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

        report_name TEXT NOT NULL,
        report_type TEXT NOT NULL,
        report_data TEXT NOT NULL,

        user_id INT NOT NULL,

        FOREIGN KEY (user_id) REFERENCES Users(ID)
        )
    '''
