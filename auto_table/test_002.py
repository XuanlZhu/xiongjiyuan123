import base64
import hashlib
data = "3KMQ9MtRMn0DQEfkPVaDqQ%3D%3D".encode("utf-8")
print(data)
a="Yll+15827540961"
a = hashlib.md5(data)
print(str(a))