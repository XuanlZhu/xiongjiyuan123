from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
from ..models import test_user
from django.http import Http404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
#解密
def decrypt_transfer(data):
    #私钥
    private_key = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC8tAOk0UgbrsYceWpdXTHlo5fp6H4WOGIeNRQIT3U2I1dgPUGY\nx7uJNdFMFcorUeV43gNCdw7/hJ0nVqsNQGFITxcl/kQ2+yJ+fCteEAoY8ceXYMyE\n4zn67WknmiDM7r/EXawtwBonCgFd5M3WTo2ky3hmpG/bBy+DaI54XWFO3wIDAQAB\nAoGAQ4Hs6co7Dzg7xJUFIciE4L/hSXt0nBNouqDHfV+bsZX8HMBdVsBhjWk06pDD\nBjNishZOuTjpoyy4ogml4PQ+uKc8fVXSV5K3t9iS5EU5V9tialGzt21sRv1AS+MG\nCE9e4uvbDSe8plBo6bGc+SOmxJpqoRq0DgPaKqrMk3ve9sECQQDJEfKyqom2FvAd\nON1ZAUbXGrSnoLkHtpT9/T2s6vaJM9skLCtzIV6CwCTaKBChE86O3rCNNwaqqulR\nVitBAB6fAkEA8EEr/4EYD86B9VTL+lwBep9fCL931a+PkDojZoEU62kb84xTT4M5\nV5i537ZjVx55rikLQqDlQ9KjrYs0pGAnwQJBAJHsDqCPl4Wou/XZMPrJLGornXQR\n9nackSCLStlVZDpKgf2MeLQDQZ3OaHBSp07fGwcgoiy6BIKTquQ2jwmLVq0CQDeF\nSA6mnZHhjiTMsMqtgmX8+HBEFwRZqtqQpOemQthYFO6GaiZA0/qLP8EUHAbg8wut\nTn3aQsEWp16Ogd7OncECQFOrH3StPV79Foi/6LBp9T6+DO9OPRNloI3G0YPUdBRI\n9rJh88RSYKDk6Rll/e8YN4JhDxbcl4AFFzrgtj0kAyY=\n-----END RSA PRIVATE KEY-----'
    data = base64.b64decode(data)
    privateKey = RSA.importKey(private_key) #载入私钥
    cipher = PKCS1_v1_5.new(privateKey)
    decrypt_data = cipher.decrypt(data,sentinel=None)#解密
    decrypt_data = decrypt_data.decode("utf-8")#转码
    return decrypt_data

#校验账号是否存在
def is_user_exist(user):
    try:
        test_user.objects.get(user=user)
    except ObjectDoesNotExist:   #捕获对象不存在异常（查询结果无数据）
        return 0
    except Exception:
        return -1
    else:
        return 1



