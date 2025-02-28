import mysql.connector as mysql

def connect():
    global mydb
    mydb = mysql.connect(
        host = "localhost",
        user = "root",
        password = ******
    )
    global mycursor
    mycursor = mydb.cursor()
    mycursor.execute("USE password_manager")

def disconnect():
    mycursor.close()

def get_login_info(username):
    sql = "SELECT * FROM accounts WHERE username = %s"
    username = (username,)
    mycursor.execute(sql, username)
    info = mycursor.fetchone()
    return(info)

def check_unique(username):
    sql = "SELECT username FROM accounts WHERE username = %s"
    username = (username,)
    mycursor.execute(sql, username)
    info = mycursor.fetchall()
    if(len(info )!= 0):
        return(False)
    else:
        return(True)
def create_account(username, password, salt):
    sql = "INSERT INTO accounts (username, password, salt) VALUES (%s, %s, %s)"
    value = (username, password, salt)
    mycursor.execute(sql, value)
    mydb.commit()
    

def get_password(search, id):
    sql = "SELECT * FROM passwords WHERE Purpose = %s AND UserID = %s"
    value = (search, id)
    mycursor.execute(sql, value)
    info = mycursor.fetchall()
    return(info)

def delete_password(search, id):
    sql = "DELETE FROM passwords WHERE Purpose = %s AND UserID = %s"
    value = (search, id)
    mycursor.execute(sql, value)
    mydb.commit()

def get_all(id):
    sql = "SELECT * FROM passwords WHERE UserID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    info = mycursor.fetchall()
    return(info)

def insert_password(password, username, purpose, id):
    sql = "INSERT INTO passwords (Username, Password, UserID, Purpose) VALUES (%s, %s, %s, %s)"
    value = (username, password, id, purpose)
    mycursor.execute(sql, value)
    mydb.commit()