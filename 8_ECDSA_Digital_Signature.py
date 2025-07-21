# ผู้ส่ง
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
print("ผู้ส่ง")
msg = b'Ratthasart'
key = ECC.generate(curve='p256')
hashed = SHA256.new(msg)
signer = DSS.new(key,'fips-186-3')
signature = signer.sign(hashed)
print("Signature :", signature)

# ผู้รับ
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
print("ผู้รับ")
msg = b'Ratthasart'
key = ECC.generate(curve='p256')
hashed = SHA256.new(msg)
verifier = DSS.new(key,'fips-186-3')
try:
    verifier.verify(hashed,signature)
    print('Authentic')
except:
    print('Not Authentic')

# ผู้ส่ง
# สร้างชื่อขึ้นมาก่อน msg = b'Ratthasart'
# เราก็จะสร้างคี์โดยใช้ key = ECC.generate(curve='p256') คือ ECC โดยใช้พารามิเตอร์ p256
# จากนั้นก็จะแฮช msg โดยใช้ SHA256 (hashed = SHA256.new(msg))
# จากนั้นก็จะสร้างสร้างวัตถุการเซ็นโดยใช้คีย์ส่วนตัว คือ signer = DSS.new(key,'fips-186-3')
# แล้วก็จะได้ signature ออกมา (signature = signer.sign(hashed))
# output : b'\x1744\xc5\x19\x16X\\J`\x04\xf0o\xb6\xcb\xe6e\x942\xc9\x8d_|\xde\xfc\xb3U\x88Q\xd1]\x0e4\x0b\xc9\xa7\x85o1\xc6\xe7\x1f\xe5\x8aj\xc4\xe3\x97\n\xde\x81\xf2n\x0c\x0e\x85\x92W\x07\xfa\xd2!p\xb6'

# ผู้รับ
# สร้างชื่อขึ้นมาก่อน msg = b'Ratthasart'
# เราก็จะสร้างคี์โดยใช้ key = ECC.generate(curve='p256') คือ ECC โดยใช้พารามิเตอร์ p256
# จากนั้นก็จะแฮช msg โดยใช้ SHA256 (hashed = SHA256.new(msg))
# จากนั้นก็จะสร้างสร้างวัตถุการเซ็นโดยใช้คีย์ส่วนตัว คือ signer = DSS.new(key,'fips-186-3')
# ทีนี้เราก็จะตรวจสอบว่าเป็น ลายเซ็นถูกต้อง หรือ ลายเซ็นไม่ถูกต้อง