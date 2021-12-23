import base64
import datetime
import hashlib
import random
import string
from .constant import *
from Crypto.Cipher import DES3


class CryptoDES3:
    def __init__(self):
        self.mode = DES3.MODE_CBC  # 加密模式
        self.BS = DES3.block_size

    def pad(self, s):
        pad_len = 8 - (len(s) % self.BS)
        s += bytes([pad_len] * pad_len)
        return s

    def un_pad(self, s):
        pad_len = s[-1]
        s = s[:-pad_len]
        return s

    def encrypt(self, text, key, iv):
        text = text.encode('utf-8')
        # 加密
        text = self.pad(text)
        cryptor = DES3.new(key, self.mode, iv)
        self.ciphertext = cryptor.encrypt(text)
        return base64.b64encode(self.ciphertext).decode("utf-8")

    def decrypt(self, text, key, iv):
        # 解密
        cryptor = DES3.new(key, self.mode, iv)
        de_text = base64.b64decode(text)
        plain_text = cryptor.decrypt(de_text)
        # print('=========== decrypt ======== plain_text : ', plain_text, ' type ', type(plain_text))
        return str(self.un_pad(plain_text).decode("utf-8"))


# 3des加密
def des_encrypt(system, data):
    if data:
        _c = CryptoDES3()
        decode_data = _c.encrypt(text=data, key=DES_KEY[system]['secretKey'].encode(),
                                 iv=DES_KEY[system]['iv'].encode())
        return decode_data

        # des_obj = pyDes.triple_des(SECRET_CONFIG[system]['secretKey'], pyDes.CBC, IV=SECRET_CONFIG[system]['iv'],
        #                            pad=None, padmode=pyDes.PAD_PKCS5)
        # encrypt_data = des_obj.encrypt(data)
        # decode_data = base64.b64encode(encrypt_data)
        # return decode_data.decode('utf-8')


# 解密
def des_decrypt(system, data):
    if data:
        # encode_data = base64.b64decode(data)
        # des_obj = pyDes.triple_des(SECRET_CONFIG[system]['secretKey'], pyDes.CBC, IV=SECRET_CONFIG[system]['iv'],
        #                            pad=None, padmode=pyDes.PAD_PKCS5)
        # decrypt_data = des_obj.decrypt(encode_data).decode('utf-8')

        _c = CryptoDES3()
        decrypt_data = _c.decrypt(text=data, key=DES_KEY[system]['secretKey'].encode(),
                                  iv=DES_KEY[system]['iv'].encode())
        # print('=========== des_decrypt ======== decrypt_data : ', decrypt_data, ' type ', type(decrypt_data))
        return decrypt_data


# md5 hash
def md5_hash(system, md5_data, md5_time):
    md5_data = DES_KEY[system]['key'] + md5_data + md5_time
    hash_data = hashlib.md5(md5_data.encode('utf-8')).hexdigest()
    return hash_data


# 返回八位随机字符串 或 时间戳 + 字符串
def eight_random_str(int_time=None, mode=1):
    """
    :param int_time:
    :param mode: 模式   1 为 随机字符串 8位   2 为 随机数字 8位
    :return:
    """
    if mode == 1:
        random_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    else:
        random_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random_str = ''.join([str(num) for num in random.sample(random_list, 8)])
    if not int_time:
        return random_str
    else:
        return str(int_time) + random_str


# md5加密
def md5_encrypt(s):
    if isinstance(s, str):
        m = hashlib.md5(s.encode())
    else:
        m = hashlib.md5(s)
    return m.hexdigest()


def cookie_de_weight(cookie):
    re_new_cookies = ''
    if cookie:
        new_cookies = cookie.split(';')
        re_new_cookies = ';'.join(list(set(new_cookies)))
    return re_new_cookies


# request headers --》dict
def headers_object_to_dict(headersObject):
    headers = {}
    for key, value in headersObject.items():
        headers[key] = value
    return headers


def get_now_strftime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def flow_sign_rsa():
    # RSA 加密
    pass
