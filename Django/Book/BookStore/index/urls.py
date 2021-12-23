from django.urls import path
from . import views

app_name='index'

urlpatterns = [
    # path('check', views.check_001),
    # path('index', views.home_001,name='index_home'),   #BookStore/home.html
    # path('check_002', views.check_002),
    # path('login', views.login),   #注册
    path('get_movies', views.get_movies),
    path('get_img', views.get_img),
    path('get_test', views.get_test),
]

