
from django.urls import path
from .views import *
urlpatterns = [
    
    path('', Home,name="home"),
    path('send_money/', send_money,name="send_money"),
    
    path('request_money/', request_money,name="request_money"),
    path('permission/<int:id>/', permission,name="permission"),
    path('approve/<int:id>/', approve,name="approve"),
    path('notifications/', notifications,name="notifications"),
    path('transactions/', transactions,name="transactions"),
    path('convert/<str:from_currency>/<str:to_currency>/<int:amount>/', convert_currency, ),
]