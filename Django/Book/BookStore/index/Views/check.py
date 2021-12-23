from django.http import HttpResponse

def is_null(fields):
    for i in fields:
        if i==None or i =="":
            return HttpResponse("字段不能为空",status=400)