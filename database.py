import mysql.connector
import bcrypt

DATABASE = mysql.connector.connect(
    host='192.168.0.220',
    user='root',
    passwd='FantaSoda123!',
    database='accountsprojectdatabase'
)

CURSOR = DATABASE.cursor()

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def create_user(username, password, email):

    sql_formula = 'SELECT * FROM users WHERE username = %s'

    CURSOR.execute(sql_formula, (username,))

    user = CURSOR.fetchone()

    if user:
        print("USER ALREADY EXISTS!")
    else:

        sql_formula = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'

        hashed_password = hash_password(password)

        CURSOR.execute(sql_formula, (username, hashed_password, email))

        DATABASE.commit()

def login_user(username, password):

    sql_formula = 'SELECT * FROM users WHERE username = %s'

    CURSOR.execute(sql_formula, (username,))

    user = CURSOR.fetchone()

    if user:
        stored_password = user[1]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            print("Login successful")
            return True
        else:
            print("Invalid password")
    else:
        print("User not found")
    return False
