from pwdlib import PasswordHash

password_hash=PasswordHash.recommended()

def hash_password(password:str):
    return password_hash.hash(password=password)

def verify_password(plain_pass:str,hashed_pass:str):
    return password_hash.verify(plain_pass,hashed_pass)

