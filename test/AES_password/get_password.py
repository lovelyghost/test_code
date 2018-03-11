# -*- coding: utf-8 -*-
# import bcrypt
#
# def bcrypt_pwd_new(pwd):
#     return bcrypt.hashpw(pwd, bcrypt.gensalt())
#
# print(bcrypt_pwd_new('uline01207102'))

import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
backend = default_backend()
key = os.urandom(32)
iv = os.urandom(16)
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
ct = encryptor.update(b"a secret message") + encryptor.finalize()
print(iv + base64.b64encode(ct))

# 解密
decryptor = cipher.decryptor()
print(decryptor.update(ct) + decryptor.finalize())

