# import random
# print(random.random())
# print(random.randint(0,9))
# random.seed('si')
# print(random.randint(0,9))


# import hashlib
# enc = hashlib.md5(b'si').digest()
# print(len(enc) * 8)
# enc = hashlib.sha256(b'si').digest()
# print(len(enc) * 8)

import hashlib, hmac
print("ผู้ส่ง")
msg = 's6506021612013'
msg = msg.encode('utf-8') # แปลง msg ให้เป็นรหัสของ utf-8
key = b's6506021612013'
hmac_val1 = hmac.new(key, msg, hashlib.sha256).hexdigest() # แปลงคีย์ที่ได้รับคือ key และ msg เป็นรหัสของ sha256 โดยใช้ hmac, hashlib
print("hmac_val1 : ", hmac_val1) # de42b3249e8a628ddba5c212ecb7d23fa029a9b31363509ee77dff137441e4ce

print("ผู้รับ")
msg = 'Ratto'
msg = msg.encode('utf-8') # แปลง msg ให้เป็นรหัสของ utf-8
key = b'Rojjanai'
hmac_val2 = hmac.new(key, msg, hashlib.sha256).hexdigest() # แปลงคีย์ที่ได้รับคือ key และ msg เป็นรหัสของ sha256 โดยใช้ hmac, hashlib
<<<<<<< HEAD
test = hmac.compare_digest(hmac_val1, hmac_val2) # เปรียบเทียบ ผู้รับ และ ผู้ส่งว่าตรงกันไหม
print("hmac_val2 : ", hmac_val2) # 51cee9642d9578e829b82f6de8c148720345cdef0429852d66ca1a48c80a7a07

print("เปรียบเทียบ hmac_val1 กับ hmac_val2 :", test) # False
=======
hmac.compare_digest(hmac_val1, hmac_val2) # เปรียบเทียบ ผู้รับ และ ผู้ส่งว่าตรงกันไหม
print("hmac_val2 : ", hmac_val2) # 51cee9642d9578e829b82f6de8c148720345cdef0429852d66ca1a48c80a7a07

# AIzaSyBgjNW0WA93qphgZW-joXVR6VC3IiYFjfo
>>>>>>> 4572963f1d1a19676e11c9b3471ca75b2ab5f9f5
