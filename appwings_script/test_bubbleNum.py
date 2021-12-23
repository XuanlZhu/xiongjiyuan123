import json
import time

import requests

from .sco_rpc_data_v import des_encrypt, md5_hash, eight_random_str
from .test_login import get_login_info


def t_bubble(entityCode, uid, pwd):
    """
    测试气泡接口
    :param entityCode: 店号
    :param uid: 账号
    :param pwd: 密码
    :return:
    """
    host = "https://appwings.pacss.hxqcgf.com"

    result = get_login_info(entityCode, uid, pwd)

    parse_data = {
        'IDNumber': result['resultData']['extraData']['certificateId'],
        'token': result['resultData']['ticket'],
        'entityCode': entityCode,
        'uid': uid
    }
    encrypt_data = des_encrypt('App', json.dumps(parse_data))
    request_data = {
        'businessEnvironment': 'release',
        'urlControl': '/business/bubbleNum',
        'encodeType': 'EC6',
        'adapter_no': '100300',
        'entityCode': entityCode,
        'uCode': uid,
        'confSystem': 'S7',
        'system_id': '100080',
        'data': encrypt_data
    }
    t = str(int(time.time()))
    request_data['time'] = t + eight_random_str()
    request_data['identityCode'] = md5_hash('App', request_data.get('data'), request_data.get('time'))
    print('气泡接口最终请求参数 :', request_data)
    a_1 = time.time()
    response = requests.post(url=f'{host}/business/bubbleNum', data=request_data)
    print('请求耗时:', time.time() - a_1)
    print('返回值：', response.text)


# appwings 请求实例
def appwings():
    # 分开请求 接口中心      /HxoaApi/App/msgCount
    # "response_info": {"method": "get",
    #                   "request_data": {"adapter_no": "", "businessEnvironment": "release", "confSystem": "S7",
    #                                    "data": "3df3yNnXkptArtYuIZRiVorr9EOPEgybyo6AJcRj/8dnZ20iq/ZTBPE30RPI2wmnh3ge4VW2o/M10F0PaeWQ3YBn4OaRxHaXlBH81PUNVQui2Guxd6Mpzlydqi3kIowsvCt9VHyoxzu6JRhKKr1nOf8U65wJiO6Pob8bN4yfmc68LGZD//iAoZVE3cVEEcTKdo/cIy68mz9gQF+gmgy9pvIhqYfYHkqt86WWjG31a42CCJMZgxdpTqj/lo0uWVr4RkOrwwoS2Muys2pRK8ri+lKTKoDqpXgxRWtjar+8y1HFoiA47Zoto7P2kR/VaCiCZt1MM49f/207yxZbigpy/GyGUqjidqq0B28CisxKMB8C0azbHpTruAnooSKdGbRXbdPQwRwXv/EH2wBMoH6LubsZSCWNUrUoo/LJNKBFnM0QL/cUV2KR16cIDeJFQ/TC/As9IKXyk0GyAPIQ6tA+SyonxwS681FJzmK5+FkSdMf/6hTAfILfXkiZPM3qrKvfG0KIjRjnUPM8I6MN0cKP7w==",
    #                                    "encodeType": "EC6", "entityCode": "HD420070",
    #                                    "identity_code": "89202b77505a75b54cd7e115a8acd539", "system_id": "100080",
    #                                    "time": "1611620543CE97A3D4", "uCode": "E0CU", "uid": "E0CU",
    #                                    "urlControl": "/HxoaApi/App/msgCount"},
    #                   "request_forwarding": "http://dms-gateway.dms-prod/apigateway/dms-appwings/HxoaApi/App/msgCount?adapter_no=&businessEnvironment=release&confSystem=S7&data=3df3yNnXkptArtYuIZRiVorr9EOPEgybyo6AJcRj%2F8dnZ20iq%2FZTBPE30RPI2wmnh3ge4VW2o%2FM10F0PaeWQ3YBn4OaRxHaXlBH81PUNVQui2Guxd6Mpzlydqi3kIowsvCt9VHyoxzu6JRhKKr1nOf8U65wJiO6Pob8bN4yfmc68LGZD%2F%2FiAoZVE3cVEEcTKdo%2FcIy68mz9gQF%2Bgmgy9pvIhqYfYHkqt86WWjG31a42CCJMZgxdpTqj%2Flo0uWVr4RkOrwwoS2Muys2pRK8ri%2BlKTKoDqpXgxRWtjar%2B8y1HFoiA47Zoto7P2kR%2FVaCiCZt1MM49f%2F207yxZbigpy%2FGyGUqjidqq0B28CisxKMB8C0azbHpTruAnooSKdGbRXbdPQwRwXv%2FEH2wBMoH6LubsZSCWNUrUoo%2FLJNKBFnM0QL%2FcUV2KR16cIDeJFQ%2FTC%2FAs9IKXyk0GyAPIQ6tA%2BSyonxwS681FJzmK5%2BFkSdMf%2F6hTAfILfXkiZPM3qrKvfG0KIjRjnUPM8I6MN0cKP7w%3D%3D&encodeType=EC6&entityCode=HD420070&identity_code=89202b77505a75b54cd7e115a8acd539&system_id=100080&time=1611620543CE97A3D4&uCode=E0CU&uid=E0CU&urlControl=%2FHxoaApi%2FApp%2FmsgCount",
    #                   "forwarding_headers": {"Accept-Language": "zh-CN,zh;q=0.9", "targetTenant": "HD420070",
    #                                          "User-Agent": "PD/6.6.0 (iPhone; iOS 13.3; Scale/2.00)",
    #                                          "Authorization": "bearer 49c6b09e-e87a-44ee-a2f1-fa15ac0035f0"}
    pass


# oa 请求实例
def oa():
    # 分开请求 OA           /dms-wfs/bpm/wfs/bill/notice
    # "response_info": {"method": "get", "request_data": {"uid": "E0CU",
    #                                                     "erpHostURL": "http://dms-gateway.dms-prod/apigateway/erp-api/messageAdapter",
    #                                                     "IDNumber": "42010519830908361X", "osVersion": "13.3",
    #                                                     "tokenType": "bearer", "deviceType": "iPhone2x",
    #                                                     "deviceModel": "iPhone XR", "entityCode": "HD420070",
    #                                                     "token": "49c6b09e-e87a-44ee-a2f1-fa15ac0035f0",
    #                                                     "uCode": "E0CU", "erpUserId": "91190000013415",
    #                                                     "appVersion": "6.6.0", "busiType": "100081"},
    #                   "request_forwarding": "http://dms-gateway.dms-prod/apigateway/dms-wfs/bpm/wfs/bill/notice?uid=E0CU&erpHostURL=http%3A%2F%2Fdms-gateway.dms-prod%2Fapigateway%2Ferp-api%2FmessageAdapter&IDNumber=42010519830908361X&osVersion=13.3&tokenType=bearer&deviceType=iPhone2x&deviceModel=iPhone+XR&entityCode=HD420070&token=49c6b09e-e87a-44ee-a2f1-fa15ac0035f0&uCode=E0CU&erpUserId=91190000013415&appVersion=6.6.0&busiType=100081",
    #                   "forwarding_headers": {"Accept-Language": "zh-CN,zh;q=0.9", "targetTenant": "HD420070",
    #                                          "User-Agent": "PD/6.6.0 (iPhone; iOS 13.3; Scale/2.00)",
    #                                          "Authorization": "bearer 49c6b09e-e87a-44ee-a2f1-fa15ac0035f0"}
    pass


# crm 请求示例
def crm():
    # 分开请求 CRM          /crm-interface/App/V1/CrmCommon/getInformNum
    # "response_info": {"method": "post",
    #                   "request_data": {"adapter_no": "", "businessEnvironment": "release", "confSystem": "S3",
    #                                    "data": "qxMNGHZNutMKL6X64+G5LhpMaaLZJywP0RXCYcXEHQbumTjJnjh3l0QKQFslBOwxBI4SBbZbiyf+90CNY+J14wnoU+p0q/xl+SyCSQRLOngxT0u+CaAx+hcMljjkbVWBFmK3umXwYjcuY2qhvMgfbC8qLTO/hMbAAphYmCKG2cUI1IQzughj96R//sZlI99iSjOZjuwH990ayW0beVgFpU5XU++w7fGfC1OUBfb/mytkvOytkXSjcu6mTIpb4Pi77lmcRzvJN8qRavpRRC/iWFTt1YZq2jEhUNnAbgBoWhAZ86fqG8/Oo7pK2bPlsrfsrV8fXuhrUKdsQUr1MhO3hE4CjpiRcM2tzC/w5ZVyJL2j48V34TYi/AEyZCR3XSF10FvK2kWb5Xf6feiDTJ4CRTNjt8U4GRS1sVdVCZPvfsO5VTfWkQcM4FA8GlsQXQvKbqwVSUbIFInGNYktmpMPiyII8akTcMOVJPT1FfzOD0bIhsuojkTN3BFkUsIkjAcU4PdtiYnrXMHbgKIwJp8OIg==",
    #                                    "encodeType": "EC6", "entityCode": "HD420070",
    #                                    "identity_code": "4c5908a96b5337973bffb2781e2eec83", "system_id": "100080",
    #                                    "time": "1611620543CE97A3D4", "uCode": "E0CU", "uid": "E0CU",
    #                                    "urlControl": "/CrmCommon/getInformNum"},
    #                   "request_forwarding": "http://dms-gateway.dms-prod/apigateway/crm-interface/App/V1/CrmCommon/getInformNum?adapter_no=&businessEnvironment=release&confSystem=S3&data=qxMNGHZNutMKL6X64%2BG5LhpMaaLZJywP0RXCYcXEHQbumTjJnjh3l0QKQFslBOwxBI4SBbZbiyf%2B90CNY%2BJ14wnoU%2Bp0q%2Fxl%2BSyCSQRLOngxT0u%2BCaAx%2BhcMljjkbVWBFmK3umXwYjcuY2qhvMgfbC8qLTO%2FhMbAAphYmCKG2cUI1IQzughj96R%2F%2FsZlI99iSjOZjuwH990ayW0beVgFpU5XU%2B%2Bw7fGfC1OUBfb%2FmytkvOytkXSjcu6mTIpb4Pi77lmcRzvJN8qRavpRRC%2FiWFTt1YZq2jEhUNnAbgBoWhAZ86fqG8%2FOo7pK2bPlsrfsrV8fXuhrUKdsQUr1MhO3hE4CjpiRcM2tzC%2Fw5ZVyJL2j48V34TYi%2FAEyZCR3XSF10FvK2kWb5Xf6feiDTJ4CRTNjt8U4GRS1sVdVCZPvfsO5VTfWkQcM4FA8GlsQXQvKbqwVSUbIFInGNYktmpMPiyII8akTcMOVJPT1FfzOD0bIhsuojkTN3BFkUsIkjAcU4PdtiYnrXMHbgKIwJp8OIg%3D%3D&encodeType=EC6&entityCode=HD420070&identity_code=4c5908a96b5337973bffb2781e2eec83&system_id=100080&time=1611620543CE97A3D4&uCode=E0CU&uid=E0CU&urlControl=%2FCrmCommon%2FgetInformNum",
    #                   "forwarding_headers": {"Accept-Language": "zh-CN,zh;q=0.9", "targetTenant": "HD420070",
    #                                          "User-Agent": "PD/6.6.0 (iPhone; iOS 13.3; Scale/2.00)",
    #                                          "Authorization": "bearer 49c6b09e-e87a-44ee-a2f1-fa15ac0035f0"}
    pass


# erp 请求示例
def erp():
    # 分开请求 ERP          /erp-api/messageAdapter adapter_no = 100095
    # "response_info": {"method": "post",
    #                   "request_data": {"adapter_no": "100095", "businessEnvironment": "release", "confSystem": "S2",
    #                                    "data": "3+9sNkBkPsLmrCJ2SEQePNxqvD5eL3GcBWv8o9Knm9xAAaJKu+nZCiNKAxUjQS260qhjyU/8YshjmGSXG3AlsTtiBu0Nx2vrbpWEfbykRQINNf9PpXHVofMOBmLbhTCn24B6cAza9Y60l46idHPkJq5lTpwq5jBV8UCkP2eUfwtwxOjLdQsP67gRmfEXjBeUTByImQ5HU/5Ncjj7hJIgbwfQ/RpZhSIqT4ma5l7k2ZnsLrXKArKeJHj8yaX3PcbVNQom5aqJnn51EweQObNeWBedxMKrpUpefE0mAMbxbKeemDu1HqefrKAC3iIBBBuRhOU0tlU28LDL9BsBnZLPDlWp7rGuY07XQloyrv+asJHH8HWf+foOFRX2jfQxeh0gb0pcihwBkKgVeNEQYC8EIt1QsE2mkNGs6t6uEg9fR2a2+MTouG9B2lAptQSSZpdnXX5ofr+4/IjOM4+VphVHWVcKzuouStuP3Mtbpq4JOV52B2lSuJJJ38Cs25vEup6ASNhx/wH+1nGdsdtjye8Ntg==",
    #                                    "encodeType": "EC6", "entityCode": "HD420070",
    #                                    "identity_code": "fc0b46654ed7d788003decfff49a5449", "system_id": "100080",
    #                                    "time": "1611620543CE97A3D4", "uCode": "E0CU", "uid": "E0CU",
    #                                    "urlControl": null},
    #                   "request_forwarding": "http://dms-gateway.dms-prod/apigateway/erp-api/messageAdapter?adapter_no=100095&businessEnvironment=release&confSystem=S2&data=3%2B9sNkBkPsLmrCJ2SEQePNxqvD5eL3GcBWv8o9Knm9xAAaJKu%2BnZCiNKAxUjQS260qhjyU%2F8YshjmGSXG3AlsTtiBu0Nx2vrbpWEfbykRQINNf9PpXHVofMOBmLbhTCn24B6cAza9Y60l46idHPkJq5lTpwq5jBV8UCkP2eUfwtwxOjLdQsP67gRmfEXjBeUTByImQ5HU%2F5Ncjj7hJIgbwfQ%2FRpZhSIqT4ma5l7k2ZnsLrXKArKeJHj8yaX3PcbVNQom5aqJnn51EweQObNeWBedxMKrpUpefE0mAMbxbKeemDu1HqefrKAC3iIBBBuRhOU0tlU28LDL9BsBnZLPDlWp7rGuY07XQloyrv%2BasJHH8HWf%2BfoOFRX2jfQxeh0gb0pcihwBkKgVeNEQYC8EIt1QsE2mkNGs6t6uEg9fR2a2%2BMTouG9B2lAptQSSZpdnXX5ofr%2B4%2FIjOM4%2BVphVHWVcKzuouStuP3Mtbpq4JOV52B2lSuJJJ38Cs25vEup6ASNhx%2FwH%2B1nGdsdtjye8Ntg%3D%3D&encodeType=EC6&entityCode=HD420070&identity_code=fc0b46654ed7d788003decfff49a5449&system_id=100080&time=1611620543CE97A3D4&uCode=E0CU&uid=E0CU&urlControl=None",
    #                   "forwarding_headers": {"Accept-Language": "zh-CN,zh;q=0.9", "targetTenant": "HD420070",
    #                                          "User-Agent": "PD/6.6.0 (iPhone; iOS 13.3; Scale/2.00)",
    #                                          "Authorization": "bearer 49c6b09e-e87a-44ee-a2f1-fa15ac0035f0"}
    pass


if __name__ == "__main__":
    # 直接请求 接口中心
    t_bubble("", "", "")
