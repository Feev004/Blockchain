# ผู้ส่ง
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
print("ผู้ส่ง")
msg = b'Ratthasart'
key = RSA.generate(2048)
hashed = SHA256.new(msg)
signature = pss.new(key).sign(hashed)
print("Signature :", signature)
print()

# ผู้รับ
print("ผู้รับ")
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
msg = b'Ratthasart'
key = RSA.generate(2048)
hashed = SHA256.new(msg)
verifier = pss.new(key)
try:
    verifier.verify(hashed, signature)
    print('Authentic')
except:
    print('Not Authentic')
print()

# ผู้ส่ง
# สร้างชื่อขึ้นมาก่อน msg = b'Ratthasart'
# เราก็จะสร้างคี์โดยใช้ key = RSA.generate(2048) คือ RSA ขนาดที่ใช้ 2048 บิต
# จากนั้นก็จะแฮช msg โดยใช้ SHA256 (hashed = SHA256.new(msg))
# จากนั้นก็จะสร้างลายเซ็นดิจิทัลโดยใช้คีย์ส่วนตัวและแฮชของข้อความ คือ signature = pss.new(key).sign(hashed)
# แล้วก็จะได้ signature ออกมา 
# output : b'\x8aJ\xd7y@\xe1\x82\xf0\x8ck\xaa\r\x16\r\xd4\xdct\t\xcb(.\xe8\x95\xda1\x86R\x04_<\x07\x19\xbd6\x1e\x0f\x95\xbb\x9a\x93Y\xeb\xdd![\xe3\xe2%\x8cB\x7fuq\x86\x97\xd4\xfbA\xeb\x1dU\xd2Avjt\x81\x16X\xdd\xd2\x85D\xf3\x88^u\xb9\x98\xe0\x0f\x1d{N1`\x9c\x1eok\xd5%\x9d\x03\xa3\x01\xfc}6\xed\xe2t\x18\xe9\xcc\xc7\xdb|M`\x8b\xf2\x0e\xbak\x03\xc0\xb5\xb0\xc5&\xab\x17*\xae\xd4{\xa5\x12\xeb\xd0\x03\t\xc2Q\xb8\xc2\x85Q\xf0\x02\xec\xec\xefE{\x9b)\xbe\xf8n\xcd[\xb0\x8c\xe3\xa1\xeatEy\xd4\x1b\x10\xa0\xf7\x19\x9e\x89\xd3\xdb\xa2\xd5J,\x19#\xc72\xc0\x9bOl\xa5\xaamU\x9d\x98\xbf\xf3\x16\xf4\xc5q\xcec\xe5c\xd9\xc0\x8a\xf8\xd5\xd0$\x11\xeb\x15g\xe9 hz\xe2\xe2\xb10\x01\x13\xca\xbc\xfb\xaf\xed!\xde\xfbo\x89\xa2\xee\xee\xed\x8e\x8a\x04\xcf\xc7\xcb\x1f\xceD\x98u\xa3\xdc\xa7L\xab\xc2\xe8G\x18\xf7\xf2'

# ผู้รับ
# สร้างชื่อขึ้นมาก่อน msg = b'Ratthasart'
# เราก็จะสร้างคี์โดยใช้ key = RSA.generate(2048) คือ RSA ขนาดที่ใช้ 2048 บิต
# จากนั้นก็จะแฮช msg โดยใช้ SHA256 (hashed = SHA256.new(msg))
# จากนั้นก็สร้างวัตถุการตรวจสอบลายเซ็นโดยใช้คีย์สาธารณะ (verifier = pss.new(key))
# ทีนี้เราก็จะตรวจสอบว่าเป็น ลายเซ็นถูกต้อง หรือ ลายเซ็นไม่ถูกต้อง