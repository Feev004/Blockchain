import hashlib
msg = 'si'
msg = msg.encode('utf-8')
enc_sha = hashlib.sha256(msg)
enc_sha.digest_size * 8 #ได้ขนาด 256 Bits
enc_sha = enc_sha.hexdigest()
print(enc_sha)