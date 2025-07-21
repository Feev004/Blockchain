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

# เริ่มแรกจะทำการสร้างคีย์ RSA ที่ขนาด 1024 บิต
# แล้วทำการสร้างทั้ง private_key และ public_key
# หลังจากนั้นก็ทำการส่งข้อความที่ต้องการที่จะเข้ารหัส msg = b'sirintra'
# จากนั้นก็สร้างคีย์เข้ารหัสใหม่ โดยใช้ public_key โดยวัตถุที่ใช้สร้างคีย์คือ cip = PKCS1_OAEP.new(public_key)
# จากนั้นก็การเข้ารหัสข้อความโดยใช้ cip (enc = cip.encrypt(msg))
# แล้วจะได้เป็นรหัสเฉพาะมา b'\x8b\x1c\x9f\x1d\x8e\x0b\x1c\x9f\x1d\x8e\x0b\x1c\x9f\x1d\x8e\x0b'

# # ถอดรหัส
# จะทำการสร้าง PKCS1_OAEP ในที่นี้คือ (dcip = PKCS1_OAEP.new(private_key))
# จากนั้นก็เอารหัสที่เราจะถอด enc มาแปลงรหัสโดยใช้ dcip (dcrypt = dcip.decrypt(enc))