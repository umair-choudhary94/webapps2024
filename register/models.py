from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import *
CURRENCY_CHOICES = (
    ('GBP', 'GB Pounds'),
    ('USD', 'US Dollars'),
    ('EUR', 'Euros'),
)

COUNTRY_CHOICES = (
    ('GB', 'United Kingdom'),
    ('US', 'United States'),
    ('EU', 'European Union'),  
)

class Userprofile(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=200)  
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP')  
    amount = models.FloatField(default=0)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email 
