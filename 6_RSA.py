from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
key = RSA.generate(1024)
private_key = key
public_key = key.publickey()
msg = b'sirintra'
cip = PKCS1_OAEP.new(public_key)
enc = cip.encrypt(msg)
print(enc)
# ถอดรหัส
dcip = PKCS1_OAEP.new(private_key)
dcrypt = dcip.decrypt(enc)
print(dcrypt)