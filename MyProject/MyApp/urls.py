from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$',views.hello,name='hello'),
url(r'register/',views.Register,name='Register'),
url(r'thanks/',views.template_thanks,name='thanks'),
url(r'log/',views.Login,name='login'),
]



