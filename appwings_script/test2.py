import time
import random
import string
import hashlib

DES_KEY = {  # 加密参数配置
    'SSO': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': 'my.oschina.net/penngo?#@',
        'iv': '01234567'
    },

    'ERP': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': 'hxqc.com/owkx.kew#kpdh32',
        'iv': '08183625'
    },

    'CRM': {
        'alg': 'des-ede3-cbc',
        'key': 'kj@fr#bgxt41@#@1-03@ffs3',
        'secretKey': '52%HF9U*lQADmir!p#FW0HHg',
        'iv': '01234567'
    },

    'OA': {
        'alg': 'des-ede3-cbc',
        'key': 'oa@12@w62t41n#b1-0fssfs0',
        'secretKey': 'hxqc.com/oadsckew#kpdhaa',
        'iv': '76543210'
    },

    'NC': {

        'alg': 'des-ede3-cbc',
        'key': 'diap$@ds%&^erwc@$^*fsvs4',
        'secretKey': 'oalx@052vos,xpedc;xo1@$6',
        'iv': '52681239'
    },

    'NSCode': {
        'alg': 'des-ede3-cbc',
        'key': '',
        'secretKey': '^0f0wo@!m6s*89^n0#&nh;d$',
        'iv': '01234567'
    },
    'Mall': {
        'alg': 'des-ede3-cbc',
        'key': '',
        'secretKey': '^0f0wo@!m6s*89^n0#&nh;d$',
        'iv': '01234567'
    },
    'App': {
    "type": "des3",
    'alg': 'des-ede3-cbc',
    'key': '2zke1@$%kaocmalzomzlajqo',
    'secretKey': 'jshyui890kxiq*9snbxhau@!',
    'iv': '01234567'
},
    'Chat': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': '9$1D7p5SFfC9FHwdVUE#-zi0',
        'iv': '01234567'
    },
    'UsedCar': {
        'alg': 'des-ede3-cbc',
        'key': 'a$%$^#w12341@#@1-03@ffs3',
        'secretKey': '9$1D7p5SFfC9FHwdVUE#-zi0',
        'iv': '01234567'
    },
    'EHR': {
        'alg': 'des-ede3-cbc',
        'key': 'cb%6^*w45@41@#@1-03@ffs3',
        'secretKey': 'hxqc.com/oadsckew#kpdhaa',
        'iv': '76543210'
    }
}

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

def md5_hash(system, md5_data, md5_time):
    md5_data = DES_KEY[system]['key'] + md5_data + md5_time
    hash_data = hashlib.md5(md5_data.encode('utf-8')).hexdigest()
    return hash_data

data = "3TQ+jlYgpZsLz1vIFL77DOHCU20iehqH4TFTq629kJPY7ZadfrproNc1EbakA+2zuLyBcGspYLvykMWsTeBlZa/C/NqOoQrneWKCX4slMO4D2wxAAAGvrgtu+hu+F1O2t1Ik06lOo20LLUWRwj0qKajJRQmrxIUEMfpN6tEAbPYDn4QZPTguGJDlijsul5akchY8fjN9/cSXaALcb2CfBRrKWyePb2x9I7gnfLwrt8dYP9i7Gj0kEubB52w3xJtrEbmll05eXDcVMzZB2jqIBHXfuz+I6+gU7jcGSs1BL1vh1/TQUWPnch2S7zS5mr8ks/Jb/d5FHaL6Sl7VpVqOzBat+ZSOkfnl6G6hO4BbdP8YD+zh5fxfb4ayLiRmSorKPBiISR+DkGRUo40iLCdYk7MCs4iZTOQKxSHGG+/FEiCWJuCVz+AIcASjUjF8rPoP5nbIrmkBmHkUGq7zOFiTZl6LqZHUxTvp9ERPE5L8o2ZjpbuintNRnw=="

time1 = str(int(time.time())) + eight_random_str()
id_code = md5_hash('App', data, time1)
print(time1)