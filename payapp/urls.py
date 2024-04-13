
from django.urls import path
from .views import *
urlpatterns = [
    
    path('', Home,name="home"),
    path('send_money', send_money,name="send_money"),
    path('request_money', request_money,name="request_money"),
    path('convert/', convert_currency, name='convert_currency'),
]