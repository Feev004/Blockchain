from Crypto.Cipher import DES
import string
import random

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)).encode('utf-8')
iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)).encode('utf-8')

enc = DES.new(key, DES.MODE_OFB, iv)
msg = b'Ratthasart'

cip = enc.encrypt(msg)
print(cip)

dcrypt = DES.new(key, DES.MODE_OFB, iv)
dcip = dcrypt.decrypt(cip)
print(dcip)

# run code --> python .\4_DES.py