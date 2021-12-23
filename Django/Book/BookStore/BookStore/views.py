from django.shortcuts import render #导入reder方法
from django.http import HttpResponse
import json



def page_view(request):
    html='<h1>欢迎来到，C语言中文网，网址是http://c.biancheng.net</h>'
    return HttpResponse(html)


def test_html(request):
    return render(request,'BookStore/test.html',{'name':'cnm中文网'})#根据字典数据生成动态模板

def home_001(request):

    return render(request,'BookStore/test.html')



