from Crypto.Cipher import DES
import string
import random

key = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)).encode('utf-8')
iv = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(8)).encode('utf-8')
# ทั้ง key และ iv จะทำการสุ่มค่าออกมาเป็นรหัสต่างๆ และจะกำหนดให้ทุกคำเป็นตัวพิมพ์เล็กหมด
# และยังสามารถแปลงค่าของ cip ให้กลับมาเป็น msg(dcip คือตัวแปลที่เก็บรหัสที่ถอดรหัสแล้ว)

enc = DES.new(key, DES.MODE_OFB, iv) # สร้างวัตถุการเข้ารหัส DES ใหม่ โดยใช้โหมด MODE_OFB
msg = b'Ratthasart' # ข้อความที่ต้องการเข้ารหัส

cip = enc.encrypt(msg) # เข้ารหัสข้อความ (msg) แล้วแปลงโดยใช้ (enc)
print(cip) # b'\xc2\x0f(\xf6\xc1\xb7\x90\xe4\x97\x02'

dcrypt = DES.new(key, DES.MODE_OFB, iv) # สร้างวัตถุการถอดรหัส DES ใหม่ โดยใช้โหมด MODE_OFB
dcip = dcrypt.decrypt(cip) # ถอดรหัสข้อความที่เข้ารหัส (cip) แล้วแปลงโดยใช้ (dcrypt)
print(dcip)
# b'Ratthasart'

# pip install pycryptodome
# run code --> python .\4_DES.py