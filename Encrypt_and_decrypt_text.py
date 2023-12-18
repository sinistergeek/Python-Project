from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex
import sys

plain_text = sys.argv[1]
key = b'this is a 16 key'
iv = Random.new().read(AES.block_size)
mycipher = AES.new(key,AES.MODE_CFB,iv)
ciphertext = iv + mycipher.encrypt(plain_text.encode())
mydecrypt = AES.new(key,AES.MODE_CFB,ciphertext[:16])
ciphertext
file_out = open("encrypted.bin","wb")
file_out.write(ciphertext[16:])
file_out.close()
print("The key k is: ",key)
print("iv is: ",b2a_hex(ciphertext)[:16])
print("The encrypted data is:",b2a_hex(ciphertext)[16:])
print("The decrypted data is:",decrypttext.decode())
