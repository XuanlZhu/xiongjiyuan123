from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, PKCS1_v1_5
import base64

#私钥
private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC8tAOk0UgbrsYceWpdXTHlo5fp6H4WOGIeNRQIT3U2I1dgPUGY\nx7uJNdFMFcorUeV43gNCdw7/hJ0nVqsNQGFITxcl/kQ2+yJ+fCteEAoY8ceXYMyE\n4zn67WknmiDM7r/EXawtwBonCgFd5M3WTo2ky3hmpG/bBy+DaI54XWFO3wIDAQAB\nAoGAQ4Hs6co7Dzg7xJUFIciE4L/hSXt0nBNouqDHfV+bsZX8HMBdVsBhjWk06pDD\nBjNishZOuTjpoyy4ogml4PQ+uKc8fVXSV5K3t9iS5EU5V9tialGzt21sRv1AS+MG\nCE9e4uvbDSe8plBo6bGc+SOmxJpqoRq0DgPaKqrMk3ve9sECQQDJEfKyqom2FvAd\nON1ZAUbXGrSnoLkHtpT9/T2s6vaJM9skLCtzIV6CwCTaKBChE86O3rCNNwaqqulR\nVitBAB6fAkEA8EEr/4EYD86B9VTL+lwBep9fCL931a+PkDojZoEU62kb84xTT4M5\nV5i537ZjVx55rikLQqDlQ9KjrYs0pGAnwQJBAJHsDqCPl4Wou/XZMPrJLGornXQR\n9nackSCLStlVZDpKgf2MeLQDQZ3OaHBSp07fGwcgoiy6BIKTquQ2jwmLVq0CQDeF\nSA6mnZHhjiTMsMqtgmX8+HBEFwRZqtqQpOemQthYFO6GaiZA0/qLP8EUHAbg8wut\nTn3aQsEWp16Ogd7OncECQFOrH3StPV79Foi/6LBp9T6+DO9OPRNloI3G0YPUdBRI\n9rJh88RSYKDk6Rll/e8YN4JhDxbcl4AFFzrgtj0kAyY=\n-----END RSA PRIVATE KEY-----'
#公钥
public_key = b'-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8tAOk0UgbrsYceWpdXTHlo5fp\n6H4WOGIeNRQIT3U2I1dgPUGYx7uJNdFMFcorUeV43gNCdw7/hJ0nVqsNQGFITxcl\n/kQ2+yJ+fCteEAoY8ceXYMyE4zn67WknmiDM7r/EXawtwBonCgFd5M3WTo2ky3hm\npG/bBy+DaI54XWFO3wIDAQAB\n-----END PUBLIC KEY-----'

print(private_key)
print(public_key)


data = 'W+/58RpnD/1gVDGm4UEntjKSnN/vy9tbcZNW8z3I1HSK77wJqxETfgOpxWu4aEpnV8T1sDkI2GwzaXmDlPlTmpu89cbuzYwfC/Ia+b9XAoDM2ArsdTzDkb/rIlQ+fz/pGIlT4UHx2/iEyFo5nGIYBinCscyLorGi6j+AR/P4PRs='
data = base64.b64decode(data)
print(data)




privateKey = RSA.importKey(private_key)
cipher = PKCS1_v1_5.new(privateKey)

b = cipher.decrypt(data,sentinel=None)
b = b.decode("utf-8")
print(b)