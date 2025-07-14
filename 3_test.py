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
msg = 'si'
msg = msg.encode('utf-8')
key = b'sirintra'
hmac_val1 = hmac.new(key, msg,
hashlib.sha256).hexdigest()