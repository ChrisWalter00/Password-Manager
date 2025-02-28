import bcrypt

def verify_pw(pw1, pw2):
    bytes = pw2.encode('utf-8')
    pw1 = pw1.encode('utf-8')
    return(bcrypt.checkpw(bytes, pw1))


def new_hash(input):
    salt = bcrypt.gensalt()
    bytes = input.encode('utf-8')
    hashed_pw = bcrypt.hashpw(bytes, salt)
    hashed_pw = hashed_pw.decode('utf-8')
    return((hashed_pw, salt))

def encrypt(password, key):

def decrypt(password, key):