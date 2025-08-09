import secure

pw = "testing_this_password"
print(pw.encode('utf-8'))
key = "test"
ciphertext = secure.encrypt(pw, key)
print("Encrypted:", ciphertext)
plaintext = secure.decrypt(ciphertext, key)
print("Decrypted:", plaintext)
ptint(test)
