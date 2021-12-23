import requests
from pacss预上线.接口.id_code import create_id_code
import time
import urllib.parse
import json

#登陆
url = "https://dms.hxqcgf.com/apigateway/auth/oauth/token?username=A0KJ&password=jDtacbufYkXgEErnaKOgfQ%3D%3D&entitycode=HD420610&isRemember=true&grant_type=password&device_type=pacss"
headers = {"authorization": "Basic c2NvOmRtcw=="}
params = {}
r = requests.get(url=url, headers=headers)
print("登陆")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息
token = "Bearer "+r.json()["access_token"]


#人员采集
url = "https://dms.hxqcgf.com/apigateway/dms-hr-basic/bd/collect"
headers = {"Authorization": token}
id_card = create_id_code()
data = {
            "psnname":"测试",
            "id_card":id_card,
            "sex":"男",
            "nationnality_id":"4064",
            "birthdate":"1991-03-23",
            "addr":"1",
            "psncl_id":"1",
            "dept_id":"4329",
            "om_job_id":"28209",
            "mobile":"17762538936",
            "wktype":"1",
            "is_elite":"0",
            "is_prob":"1",
            "prob_month":"1",
            "begindate":"2021-03-01",
            "enddate":"2021-03-31",
            "photo":"",
            "id":id_card
}
r = requests.post(url=url, headers=headers, data=data)
print("人员采集")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息

#查询psn_id
url = "https://dms.hxqcgf.com/apigateway/dms-hr-basic/bd/collect?page=1&rows=1"
headers = {"Authorization": token}
params = {}
r = requests.get(url=url, headers=headers)
print("查询psn_id")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息
print(r.json()["data"]["data"][0]["psndoc_id"])

#转入
url = "https://dms.hxqcgf.com/apigateway/dms-hr-basic/bd/collect/movepsn"
headers = {"Authorization": token}
data = {"psndoc_id[0]":r.json()["data"]["data"][0]["psndoc_id"]}
r = requests.post(url=url, headers=headers, data=data)
print("转入")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息

time.sleep(15)
#查询账号
url = f"https://dms.hxqcgf.com/apigateway/admin/user/getUserInfoList?limit=20&offset=0&searchData=%7B%22certificateId%22:%22{id_card}%22%7D"
headers = {"Authorization": token}
params = {}

r = requests.get(url=url, headers=headers,params=params)
print("查询账号")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息
print("HD340400",r.json()['data']['list'][0]['employee_no'],id_card[-7:-1])


