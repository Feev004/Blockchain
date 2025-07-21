# ผู้ส่ง
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
print("ผู้ส่ง")
msg = b'Ratthasart'
key = RSA.generate(1024)
hashed = SHA256.new(msg)
signature = pss.new(key).sign(hashed)
print()

# ผู้รับ
print("ผู้รับ")
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
msg = b'sirintra'
key = RSA.generate(1024)
hashed = SHA256.new(msg)
verifier = pss.new(key)
try:
    verifier.verify(hashed, signature)
    print('Authentic')
except:
    print('Not Authentic')
print()