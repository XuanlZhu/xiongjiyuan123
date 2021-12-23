import time

localtime = time.localtime()
print(localtime)

a = time.strftime("%H%M%S", time.localtime())
print(a)
