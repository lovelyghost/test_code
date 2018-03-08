
import bcrypt

def bcrypt_pwd_new(pwd):
    return bcrypt.hashpw(pwd, bcrypt.gensalt())

print(bcrypt_pwd_new('uline01207102'))