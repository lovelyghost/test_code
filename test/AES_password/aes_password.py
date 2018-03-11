# -*- coding: utf-8 -*-
import codecs
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode
import random
import string
import binascii
import StringIO
import os

# 进件时商户支付 key 随机生成
mch_pay_key = os.urandom(16).encode('hex').upper()


def gen_randown_mch_pkey(len=32):
    return codecs.encode(os.urandom(len), 'hex').decode()[:len]


def padding(text):
    output = StringIO.StringIO()
    val = 16 - (len(text) % 16)
    for _ in xrange(val):
        output.write('{:x}'.format(val))
    return text + binascii.unhexlify(output.getvalue())


backend = default_backend()

iv = ''.join(random.choice(string.ascii_letters) for i in range(16))

dt_api_key = '30ea1aad219de0790b3b4ac9f7d53748'

cipher = Cipher(algorithms.AES(str(dt_api_key)),
                modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()
print(padding(str('81a09b329f703454c0f018e2d4d19de4')))
ct = encryptor.update(padding(str('81a09b329f703454c0f018e2d4d19de4'))) + encryptor.finalize()
print(ct)
print(iv + b64encode(ct))
