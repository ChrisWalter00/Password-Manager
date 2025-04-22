import mySQL
import secure
from getpass import getpass
def main():
    mySQL.connect()
    op = int(input("Please Choose Login (1) or Create account (2): ")) # 1 for login, 2 for create account
    if op == 1:
        key = None
        while key == None:
            key, id = login() #attempt to login, if successful, key and user id are returned
        log_out = False
        while(not log_out): #loop until user logs out
            print("Welcome to the Password Manager")
            choice = int(input("Choose from the List: \n (1) Add password\n (2) Find Password \n (3) Display All Passwords \n (4) Delete Password \n (5) Generate Password\n (6) Exit\n"))
            match choice:
                case 1: #add password
                    new_pword = input("Enter Password: ")
                    username = input("Enter Username: ")
                    purpose = input("Enter the purpose for the password (Amazon, gmail, etc.): ")
                    encrypted_pword = secure.encrypt(new_pword, key)
                    mySQL.insert_password(encrypted_pword, username, purpose, id)
                case 2: #find password
                    purpose = input("Enter the purpose for the password (Amazon, gmail, etc.): ")
                    encrypted_pword = mySQL.get_password(purpose, id)
                    pword = secure.decrypt(encrypted_pword, key)
                    print(pword)
                case 3:#display all passwords
                    encrypted_pword = mySQL.get_all(id)
                    for i in encrypted_pword:
                        pword = secure.decrypt(i, key)
                        print(pword)
                case 4:#delete password
                    purpose = input("Enter the purpose for the password (Amazon, gmail, etc.): ")
                    mySQL.delete_password(purpose, id)
                    print("Password deleted")
                case 5:#generate password
                    length = int(input("Enter the length of the password: "))
                    password = secure.generate_password(length)
                    print(password)
                case 6:#exit
                    print("Logging out...")
                    log_out = True

    else:
        create_account()
    mySQL.disconnect()#close the connection to the database
    print("Goodbye!")

        


def login(): #attempt to login
    #get username and password from user
    username = input("Username: ")
    given_password = getpass("Password: ")
    info = mySQL.get_login_info(username)
    if(info):
        id, username, stored_password, salt = info
        if(secure.verify_pw(stored_password, given_password)):#check if password is correct
            #if password is correct, return the key and user id
            print("Successful Login!")
            return(given_password, id)
    print("Wrong Username/Password")#if password is incorrect
    return
    

def create_account():#create a new account
    #get username and password from user
    unique = False
    while not unique:
        username = input("Please enter unique username: ")
        unique = mySQL.check_unique(username)#check if username is unique
        if(not unique):
            print("Username taken")#if username is not unique
    password = input("Enter Password: ")#get password from user
    password, salt = secure.new_hash(password)#hash the password
    mySQL.create_account(username, password, salt)#create account in database
    print("Account created!")#if account is created successfully



if __name__ == '__main__':
    main()
    