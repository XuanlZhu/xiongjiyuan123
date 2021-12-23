import requests
import json

r = requests.get('https://github.com/Ranxf')       # 最基本的不带参数的get请求
r1 = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})      # 带参数的get请求

url_params = {'key':'value'}     #    字典传递参数，如果值为None的键不会被添加到url中
r = requests.get('https://www.baidu.com/',params = url_params)
print(r.url)

r.encoding                       #获取当前的编码
r.encoding = 'utf-8'             #设置编码
r.text                           #以encoding解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码。
r.content                        #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。

r.headers                        #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None

r.status_code                     #响应状态码
r.raw                             #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()
r.ok                              # 查看r.ok的布尔值便可以知道是否登陆成功
 #*特殊方法*#
r.json()                         #Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
r.raise_for_status()             #失败请求(非200响应)抛出异常

r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))   #发送json请求
print(r.json())


#定制头和cookie信息
data = {'some': 'data'}
cookies = {"cookie的name":"cookie的value"}
headers = {'content-type': 'application/json',
           'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers,cookies=cookies)

print(r.text)

#响应状态码
print(r.status_code)                               # 获取返回状态
print(r1.text)        # 打印解码后的返回数据

#响应
r.headers                                  #返回字典类型,头信息
r.requests.headers                         #返回发送到服务器的头信息
r.cookies                                  #返回cookie
r.history                                  #返回重定向信息,当然可以在请求是加上allow_redirects = false 阻止重定向

#超时
r = requests.get('url',timeout=1)           #设置秒数超时，仅对于连接有效

#会话对象，能够跨请求保持某些参数
s = requests.Session()
s.auth = ('auth','passwd')
s.headers = {'key':'value'}
r = s.get('url')
r1 = s.get('url1')


#代理
#如果代理需要用户名和密码，则需要这样：
proxies = {
    "http": "http://user:pass@10.10.1.10:3128/",
}

proxies = {'http':'ip1','https':'ip2' }
requests.get('url',proxies=proxies)
