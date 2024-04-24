from django.db import models

# Create your models here.
from register.models import Userprofile,CURRENCY_CHOICES
STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Success', 'Success'),
    ('Cancelled', 'Cancelled'),
)

class reqeusted_money(models.Model):
    From = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='sent_requests')  
    to = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='received_requests')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP') 
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES,default='Pending')
    