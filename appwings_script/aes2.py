import base64
from Crypto.Cipher import AES
from .constant import AES_KEY


class AesEncrypt(object):
    def __init__(self):
        self.key = AES_KEY['secretKey'].encode('utf8')
        self.mode = AES.MODE_CBC
        self.iv = AES_KEY['iv'].encode('utf8')

    def pad(self, data):
        length = 16
        count = len(data)
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 0
        return data + ('\0' * add)

    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 字符串补位
        data = self.pad(data)
        encrypted_bytes = cipher.encrypt(data.encode('utf8'))
        # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
        encode_str = base64.b64encode(encrypted_bytes)
        # 对byte字符串按utf-8进行解码
        enctext = encode_str.decode('utf8')
        return enctext

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, data):
        data = data.encode('utf8')
        encode_bytes = base64.decodebytes(data)
        # 将加密数据转换位bytes类型数据
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        text_decrypted = cipher.decrypt(encode_bytes)
        # 去补位
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted.rstrip('\0')


if __name__ == '__main__':
    customer_id = "318393"
    e = AesEncrypt().encrypt(customer_id)
    print(e)
    d = AesEncrypt().decrypt(e)
    print(d)
