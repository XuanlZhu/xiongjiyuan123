from django.shortcuts import render #导入reder方法
from django.http import HttpResponse
import json
from .Views.login import decrypt_transfer,is_user_exist
from .models import test_user
from .models import movies as models_movies
from django.db import DataError
from .Views.check import is_null

def check_001(request):
    user = request.POST['user']
    passwd = request.POST['passwd']
    print(user,passwd)
    result = {"user": user, "passwd": passwd}
    return HttpResponse(json.dumps(result), content_type="application/json")

def home_001(request):
    return render(request,'BookStore/home.html')

def check_002(request):
    data = json.loads(request.body.decode())     #json转字典
    print(data)
    user = data["user"]
    passwd = data["passwd"]
    passwd = decrypt_transfer(passwd) #解码
    print(passwd)

    passwd_real = test_user.objects.only('passwd').get(user=user)  #根据账号查密码

    if passwd == passwd_real.passwd:
        return HttpResponse(json.dumps("登陆成功"), content_type="application/json")
    else:
        return HttpResponse(json.dumps("登陆失败"), content_type="application/json")

def login(request):
    data = json.loads(request.body.decode())  # json转字典
    user = data["user"]
    # 校验账号是否存在
    if is_user_exist(user) ==1:
        return HttpResponse(json.dumps({"msg":"账号已存在"}), content_type="application/json",status=400)
    elif is_user_exist(user) ==-1:
        return HttpResponse(json.dumps("未知错误"), content_type="application/json",status=400)
    else:
        passwd = data["passwd"]
        passwd = decrypt_transfer(passwd)  # 解码
        print(passwd)
        test_user.objects.create(user=user, passwd=passwd)

        # try:
        #     test_user.objects.create(user=user, passwd=passwd)
        # except DataError:
        #     return HttpResponse(json.dumps("密码太短"), content_type="application/json")

        return HttpResponse(json.dumps("注册成功"), content_type="application/json")

def get_movies(request):
    data = models_movies.objects.values()
    return HttpResponse(json.dumps(list(data)), content_type="application/json")

def get_img(request):
    img = request.GET["img"].strip("\u202a")
    with open(img,'rb') as f:
        return HttpResponse(f.read(), content_type="image/png")

def get_test(request):
    pass
    return HttpResponse(status=400)