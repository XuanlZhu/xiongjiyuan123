from django.db import models

# python manage.py makemigrations  生成表单数据
# python manage.py migrate    创建表


class test_user(models.Model): #创建用户信息表
    user = models.CharField(max_length=16,verbose_name='账号',unique=True,blank=False,null=False)  #verbose_name设置此字段在 admin 后台管理系统界面上的显示名称
    passwd = models.CharField(max_length=32,verbose_name='密码')
    valid = models.IntegerField(default=1,verbose_name='生效')   #1有效，0无效

class movies(models.Model): #电影表
    m_id = models.CharField(max_length=16)  #verbose_name设置此字段在 admin 后台管理系统界面上的显示名称
    name = models.CharField(max_length=32)
    img = models.CharField(max_length=32)   #1有效，0无效
    path = models.CharField(max_length=64)

