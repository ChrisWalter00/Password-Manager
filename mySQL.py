import mysql.connector as mysql

#connect to the database
def connect():
    global mydb
    mydb = mysql.connect(
        host = "localhost",
        user = "root",
        password = "Cw-985342"
    )
    global mycursor
    mycursor = mydb.cursor()
    mycursor.execute("USE password_manager")

#close the connection to the database
def disconnect():
    mycursor.close()

#get login info from the database
def get_login_info(username):
    sql = "SELECT * FROM accounts WHERE username = %s"
    username = (username,)
    mycursor.execute(sql, username)
    info = mycursor.fetchone()
    return(info)

#check if username is unique
def check_unique(username):
    sql = "SELECT username FROM accounts WHERE username = %s"
    username = (username,)
    mycursor.execute(sql, username)
    info = mycursor.fetchall()
    if(len(info )!= 0):
        return(False)
    else:
        return(True)

#create a new account in the database
def create_account(username, password, salt):
    sql = "INSERT INTO accounts (username, password, salt) VALUES (%s, %s, %s)"
    value = (username, password, salt)
    mycursor.execute(sql, value)
    mydb.commit()
    
#find a password in the database that matches the given purpose and user id
def get_password(search, id):
    sql = "SELECT * FROM passwords WHERE Purpose = %s AND UserID = %s"
    value = (search, id)
    mycursor.execute(sql, value)
    info = mycursor.fetchall()
    return(info)

#delete a password in the database that matches the given purpose and user id
def delete_password(search, id):
    sql = "DELETE FROM passwords WHERE Purpose = %s AND UserID = %s"
    value = (search, id)
    mycursor.execute(sql, value)
    mydb.commit()

#get all passwords in the database that match the given user id
def get_all(id):
    sql = "SELECT * FROM passwords WHERE UserID = %s"
    value = (id,)
    mycursor.execute(sql, value)
    info = mycursor.fetchall()
    return(info)

#insert a password into the database
def insert_password(password, username, purpose, id):
    sql = "INSERT INTO passwords (Username, Password, UserID, Purpose) VALUES (%s, %s, %s, %s)"
    value = (username, password, id, purpose)
    mycursor.execute(sql, value)
    mydb.commit()