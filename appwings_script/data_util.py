from .sco_rpc_data_v import des_decrypt, des_encrypt, md5_hash, eight_random_str
import json
import time


def decode_data(system, data):
    decrypt = des_decrypt(system=system, data=data)
    print('decode_data-->: ', decrypt)


def generator_request_data(system, request_data=None, biz_data=None):
    """
    生成请求参数
    :param system: 系统 对应 constant.py:276 DES_KEY
    :param request_data: 公共请求参数
    :param biz_data: 业务请求参数
    :return:
    """
    if biz_data is None:
        biz_data = {}
    if request_data is None:
        request_data = {}
    t = str(int(time.time()))
    encrypt_data = des_encrypt(system, json.dumps(biz_data))
    request_data['time'] = t + eight_random_str()
    request_data['data'] = encrypt_data
    request_data['identityCode'] = md5_hash('App', request_data.get('data'), request_data.get('time'))
    print('最终请求参数 :', request_data)
