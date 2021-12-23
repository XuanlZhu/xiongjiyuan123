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

SYSTEM_SECRET = {
    'S1': 'SSO',
    'S2': 'ERP',
    'S3': 'CRM',
    'S4': 'NC',
    'S5': 'OA',
    'S6': 'Mall',
    'S7': 'App',
    'S8': 'Chat',
    'S9': 'UsedCar',
    'S10': 'EHR',
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

data = "ovK6QES6jDE9D+pJI/6juxxiVF6ppfyyFeZzwNs7k5vEdlIvwAAko4eLO2gnUggak6RX1spBYgGa/aw66Nj+J7oY8fY2xje45/85bwmjXQS1jm6YPN9AyPGYLDaBnDY/BJ6yR7bGrxHYj5pmTm63wXuYqGuJlyvJDOUEYd4znudonqCnJ6p57bQP/hBgM+Abur0N5wLsKTX85wBreZ83agNenVD7M6VbYAHvkd6tMWubiMYArHm+N0ONZlki5QwSgO5JsiQMb2+xwCHpJ8KtwONyJkq4Yr323K1slyE/voYCX0B36QS4td5L85Iusvq4dPyivWLzoE5eGjvsU82xYvxDHyjsF+FZmKbzu80hj6HKAPpdNtOCfa1sOfx4ynujtuA1YPGO0wSE3JgVD2R097lkQ0Gx6G82/VqolGU+ZurEaGJWavB2Tbqli52pUWJPfA0gIGgjNyCFUrNMb7MMhrRTbvF7Ujbo2rHi9HUaBdfh2GR+bDrq1WtDN10hkywPWkNWMiYK93qhuQv/hdeUYM0odIKZlP/pOKvCKjeGeDv8jnDTlrK2LlSSlYgQiJ22bjb0+qxQzIkC3rqVZBKDmKZ/k3/Pvj0aoJZhGxCBpvCC56cMO2mPno7UVZPVvrocUKu5YSID9yphN7FZsj8EwEmFpzIJ7si5mRHJECcEFRw+eoWTuwlTDmKC1mhJGLD1xEXUdI0Q3seEzjpx0/gBPg4siTqQdck+L2ZzWIzbtzty3CwyVaH5YZSv+aQNBLYaBvBKzV0MS/7KA6nSeAGiwJFpoRrG9KqLfeJ3jA7NbGRJAoWl2ygOVU8+mRPdsLaorh8Rl3PNLwQm1iGq8sYrqR+x28vkz6vw6oDiQn26ef8R2q9Steu6YM6pfGhN+qYzfmUgTTxtgC3aZycL+DA8LaaPg++bfiva1lgo56mbWolV1Mr9Clr6tKRaE5Jx014NM6jN/vXbKi0k+CgY2aI7q0cInSsgadEEs23BJqCMgSF83qeY4/x9YfPOkS2aVSvbXe2B/31/g/c6ZCCZ6zTvgmkbG4BDhDHyP8fQEUr+9FBrl/qxOWWmiuWFa7iLhzisPhf8GRcUNGdXQIr5Fv4zcSeT4jKrO47ESNEwLO2PNJBigX3j9r6m/RZ5CGRDV/E7NtOcvgGcHk5diadj0x/3zv26aaxBo8WIsZHfOj0772G7AU+YMIx5rD8xR7rLNRMIOn98OJ2tbNtrmF99bswqrdAVnWgDfohv1P0azHYQ/xgmCT5jUQUtIZVCRjdRaiY4ED6H6bp9hicRUPtA8xpesfdQbz5JlrX607jgcDmbwttIrqcB04LTm4bwSC5K9/xbyOrLLIZptoQSiEJLYXJbG/hEi12Uj1lSnuH0bXbjc8PcbjzaE3M0+nr46LSuvteXONSworDner6hfPVQDvdW2Ea6EH5pfafFjGNLCnLDFcFz/hXhHUsAYGZTGbBcYeCsOlB35ibRAfGDbcarjpd0A2/sL10JDIA+NTH2dc7zLFmEvNeu5/z7E9yPV2uLGql850SF55nuI4B/t0RGzhffg1SCHpNZ9+alEGaU77JF0TspIgSznW4o7+uxuYBIi43lDpRZpUcpXV7e6T9YehLTRxmCbo+GYw2OHXlEMOunnWuwk/a7L8VGyPEmRbK/C8puExx3S7EeWt57JRhbgGkIvw34tgfkqGWSalulK0dXoAN5vgWYsZknGt5oqa0GGZryLq/S55JVYpLJK1JobK3DykYM/KxQ1YVX3CNNSgoX/wrGsn5ChO+/Rd0msUspiUEfaMpRGVt/c4ay0JwalNh9dA2lxHtARQSjVuE0O3H2dmVnzrB20EfUbTF4P+4/K1jMLlXxeJJlFQY="

time1 = str(int(time.time())) + eight_random_str()
id_code = md5_hash('EHR', data, time1)

