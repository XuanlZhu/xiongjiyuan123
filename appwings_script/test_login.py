import json
import time
from .sco_rpc_data_v import des_encrypt, md5_hash, eight_random_str
import requests

now_time = str(int(time.time())) + eight_random_str()


def get_login_info(entity_code, uid, pwd, env='release'):
    """
    获取登录信息
    :param entity_code: 店号
    :param uid: 账号
    :param pwd: 密码
    :param env: 环境
    :return: 登录信息
    """
    now_time1 = str(int(time.time())) + eight_random_str()
    old_data = {
        "deviceType": "Android",
        "appVersion": "5.33.0",
        "debug": False,
        "entityCode": entity_code,
        "deviceVersion": 28,
        "ticket": "",
        "pswd": pwd,
        "grant_type": "password",
        "username": uid,
        "osVersion": "9",
        "deviceModel": "Redmi Note 8 Pro",
        "aid": "100080",
        "IDNumber": "",
        'tokenType': 'bearer'
    }
    data = {'isEncrypt': False, 'adapter_no': '', 'confSystem': 'S1', 'entityCode': entity_code,
            'data': des_encrypt('SSO', json.dumps(old_data)), 'system_id': '100080',
            'identity_code': '', 'uCode': uid, 'encodeType': 'EC1',
            'urlControl': '/sso/sso/getTicket.do', 'businessEnvironment': env, 'time': now_time1, 'aid': '100080'}
    md5_data = md5_hash('SSO', data['data'], now_time1)
    data['identity_code'] = md5_data

    headers = {
        'User-Agent': 'HXMall Android android HXQC iPhone iphone',
        'targetTenant': 'HD340400',
        'Authorization': '',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    url = 'https://appwings.pacss.hxqcgf.com'
    a_time = time.time()

    response = requests.get(url=url, headers=headers, params=data)
    print('时间: ', time.time() - a_time)
    print(response)
    response_data = json.loads(response.text)
    print(response_data)
    return response_data


if __name__ == '__main__':
    get_login_info('', '', '')
