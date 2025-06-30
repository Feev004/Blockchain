import hashlib, hmac
msg1 = 'few'
msg1 = msg1.encode('utf-8')
key = b'ratthasart'
hmac_val1 = hmac.new(key, msg1, hashlib.sha256).hexdigest()
print("hmac_val1 : ", hmac_val1)

import hashlib, hmac
msg2 = 'ratto'
msg2 = msg2.encode('utf-8')
key = b'ratthasart'
hmac_val2 = hmac.new(key, msg2,hashlib.sha256).hexdigest()
hmac.compare_digest(hmac_val1,hmac_val2)
print("hmac_val2 : ", hmac_val2)

# Example: Rename 'few' to 'few_renamed' and compute new HMAC
msg3 = 'few_renamed'
msg3 = msg3.encode('utf-8')
key3 = b'ratto'
hmac_val3 = hmac.new(key3, msg3, hashlib.sha256).hexdigest()
# hmac.compare_digest(hmac_val3, hmac_val1)
print("hmac_val3 (few_renamed):", hmac_val3)