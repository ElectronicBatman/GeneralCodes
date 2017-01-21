from Crypto.Cipher import XOR
import base64

def encrypt(key, plaintext):
  cipher = XOR.new(key)
  return base64.b64encode(cipher.encrypt(plaintext))

def decrypt(key, ciphertext):
  cipher = XOR.new(key)
  return cipher.decrypt(base64.b64decode(ciphertext))
mac = '4C:72:B9:21:06:B7'
a=encrypt('notsosecretkey', mac)
print a
b=decrypt('notsosecretkey', a)
print b
