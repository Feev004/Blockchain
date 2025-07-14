from Crypto.Cipher import AES
import random, string
key = ''.join(random.choice(string.ascii_uppercase +
string.ascii_lowercase + string.digits) for x in
range(32)).encode('utf-8')

iv = ''.join(random.choice(string.ascii_uppercase +
string.ascii_lowercase + string.digits) for x in
range(16)).encode('utf-8')
enc = AES.new(key, AES.MODE_OFB, iv)
msg = b'Ratthasart'
cip = enc.encrypt(msg)
print(cip)

dcrypt = AES.new(key, AES.MODE_OFB, iv)
dcip = dcrypt.decrypt(cip)
print(dcip)

# run code --> python .\5_AES.py