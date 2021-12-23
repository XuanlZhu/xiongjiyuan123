import urllib.parse
import json
from pacss测试线.id_code import create_id_code
import requests

#登陆
url = "https://dms.t.hxqcgf.com/apigateway/auth/oauth/token?username=A04L&password=QLomgFGYMWCiBg953bt8Mw%3D%3D&entitycode=HD340400&isRemember=true&grant_type=password&device_type=pacss"
headers = {"authorization": "Basic c2NvOmRtcw=="}
params = {}
r = requests.get(url=url, headers=headers)
print("登陆")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息
token = "Bearer "+r.json()["access_token"]

#获取人员信息
url = "https://dms.t.hxqcgf.com/apigateway/dms-hr-basic/bd/psn?page=752&pageSize=1&company_id=166&psnclscope=0&dept_id=&hasChild=0&indocflag=Y&login_date=2021-03-25"
headers = {"Authorization": token}
params = {}
r = requests.get(url=url, headers=headers)
print("获取code")
print(r.status_code)  # 获取响应状态码
print(r.json())  # 获取响应消息