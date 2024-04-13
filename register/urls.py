
from django.urls import path
from .views import * 
urlpatterns = [
    
    path('login/',login_now,name="login"),
    path('register/',register_now),
    path('logout/', logout_view, name='logout'),
    path('welcomepage/',welcome_page,name='welcome'),
    
]