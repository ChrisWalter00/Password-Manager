import mySQL
import secure
from getpass import getpass
def main():
    mySQL.connect()
    op = int(input("Please Choose Login (1) or Create account (2): "))
    if op == 1:
        key = None
        while key == None:
            key = login()
        log_out = 0
        while(not log_out):
            choice = input("Choose from the List: \n (1) Add password\n (2) Find Password \n (3) Display All Passwords \n (4) Delete Password \n (5) exit\n")
    else:
        create_account()
    mySQL.disconnect()

        


def login():
    username = input("Username: ")
    given_password = getpass("Password: ")
    info = mySQL.get_login_info(username)
    if(info):
        id, username, stored_password, salt = info
        if(secure.verify_pw(stored_password, given_password)):
            print("Successful Login!")
            return(given_password)
    print("Wrong Username/Password")
    return
    

def create_account():
    unique = False
    while not unique:
        username = input("Please enter unique username: ")
        unique = mySQL.check_unique(username)
        if(not unique):
            print("Username taken")
    password = input("Enter Password: ")
    password, salt = secure.new_hash(password)
    mySQL.create_account(username, password, salt)



if __name__ == '__main__':
    main()
    