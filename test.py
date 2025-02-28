#import mysql.connector as mysql

#mydb = mysql.connect(
#    host = "localhost",
#    user = "root",
#    password = "Cw-985342"
#)

#mycursor = mydb.cursor()
#mycursor.execute("SHOW DATABASES")
#for x in mycursor:
#    print(x)
#print("done")
import bcrypt
salt1 = bcrypt.gensalt()
salt2 = bcrypt.gensalt()
username1 = "test"
username2 = "test"
b1 = username1.encode('utf-8')
b2 = username2.encode('utf-8')
hash1 = bcrypt.hashpw(b1, salt1)
hash2 = bcrypt.hashpw(b2, salt2)
print(hash1)
print (salt1)
print(hash2)
