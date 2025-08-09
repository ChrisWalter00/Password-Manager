import bcrypt
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

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
    key = get_key(key)
    cipher = AES.new(key, AES.MODE_CBC, iv=key)#create the cipher
    ciphertext = cipher.encrypt(pad(password.encode('utf-8'), AES.block_size)) #ENcrypt the password
    return b64encode(ciphertext).decode('utf-8')  # Return as a string for storage
def decrypt(password, key):#Decrypt the password using the key
    key = get_key(key)
    password = password.encode('utf-8')  # Ensure the password is in bytes
    password = b64decode(password)  # Decode the base64 encoded string
    cipher = AES.new(key, AES.MODE_CBC, iv=key)#create the cipher
    plaintext = unpad(cipher.decrypt(password), AES.block_size)  #Unpad the and decrypt the password
    return plaintext.decode('utf-8')
def generate_password(length=12):#Generate a random password of the given length
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
def get_key(unencoded_key):#Get the key from the unhashed password
    if(len(unencoded_key) < 16):
        unencoded_key += '0' * (16 - len(unencoded_key))
    key = unencoded_key.encode('utf-8')
    return key[:16]  # AES requires a key of length 16, 24, or 32 bytes