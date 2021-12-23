from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5

key = RSA.generate(1024)
encrypted_key = key.exportKey()
pb_key = key.publickey().exportKey()

print(encrypted_key)
print(pb_key)

publicKey = RSA.importKey(pb_key)
cipher = PKCS1_v1_5.new(publicKey)
data = "尼玛"
data = data.encode("utf-8")


encryptedData = cipher.encrypt(data)
print(encryptedData)


privateKey = RSA.importKey(encrypted_key)
cipher = PKCS1_v1_5.new(privateKey)

b = cipher.decrypt(encryptedData,sentinel=None)
b = b.decode("utf-8")
print(b)


