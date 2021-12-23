from django.conf.urls import url
from django.contrib import admin
from django_001 import views


urlpatterns=[
    url(r'admin/', admin.site.urls),
    url(r'^page$/', views.page_view), ]