# Example: Rename 'few' to 'few_renamed' and compute new HMAC
import hashlib, hmac
msg3 = 'few_renamed'
msg3 = msg3.encode('utf-8')
key = b'ratthasart'
hmac_val3 = hmac.new(key, msg3, hashlib.sha256).hexdigest()
print("hmac_val3 (few_renamed):", hmac_val3)