from Crypto.Cipher import AES
import random, string

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(32)).encode('utf-8')
iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16)).encode('utf-8')
# ทั้ง key และ iv จะทำการสุ่มค่าออกมาเป็นรหัสต่างๆ และจะกำหนดให้ทุกคำเป็นตัวพิมพ์เล็กหมด
# และยังสามารถแปลงค่าของ cip ให้กลับมาเป็น msg(dcip คือตัวแปลที่เก็บรหัสที่ถอดรหัสแล้ว)


enc = AES.new(key, AES.MODE_OFB, iv) # สร้างวัตถุการเข้ารหัส AES ใหม่ โดยใช้โหมด MODE_OFB
msg = b'Ratthasart' # ข้อความที่ต้องการเข้ารหัส

cip = enc.encrypt(msg) # เข้ารหัสข้อความ (msg) แล้วแปลงโดยใช้ (enc)
print(cip) # b'\x85\xa1\xb5\xb8\xcf\xc4\xb7S{\xc9'

dcrypt = AES.new(key, AES.MODE_OFB, iv) # สร้างวัตถุการถอดรหัส AES ใหม่ โดยใช้โหมด MODE_OFB
dcip = dcrypt.decrypt(cip) # ถอดรหัสข้อความที่เข้ารหัส (cip) แล้วแปลงโดยใช้ (dcrypt)
print(dcip) # b'Ratthasart'

# pip install pycryptodome
# run code --> python .\5_AES.py