import bcrypt
from Crypto.Cipher import AES

def verify_pw(pw1, pw2):#check if password is correct
    bytes = pw2.encode('utf-8')
    pw1 = pw1.encode('utf-8')
    return(bcrypt.checkpw(bytes, pw1))


def new_hash(input):#hash the password
    salt = bcrypt.gensalt()
    bytes = input.encode('utf-8')
    hashed_pw = bcrypt.hashpw(bytes, salt)
    hashed_pw = hashed_pw.decode('utf-8')
    return((hashed_pw, salt))

def encrypt(password, key):#Encrypt the password using the key
    pass
def decrypt(password, key):#Decrypt the password using the key
    pass
def generate_password(length=12):#Generate a random password of the given length
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password