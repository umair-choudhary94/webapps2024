from django.db import models

# Create your models here.
from register.models import Userprofile,CURRENCY_CHOICES
STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Success', 'Success'),
    ('Cancelled', 'Cancelled'),
)
NOTIFICATIONS_CHOICES = (
    ('Request', 'Request'),
    ('Received', 'Received'),
    
)

class reqeusted_money(models.Model):
    From = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='sent_requests')  
    to = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='received_requests')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP') 
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES,default='Pending')
    
class Transaction_History(models.Model):
    Sender = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='sender')  
    Reciver = models.ForeignKey(Userprofile, on_delete=models.CASCADE, related_name='Receiver')
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP') 
    amount = models.FloatField(default=0)
    rate = models.FloatField(default=1.0)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES,default='Pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Notifications(models.Model):
    to = models.ForeignKey(Userprofile, on_delete=models.CASCADE,related_name='to_user')
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE,related_name='from_user')
    amount = models.FloatField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='GBP')
    notification_type = models.CharField(max_length=20,choices=NOTIFICATIONS_CHOICES,default='Request')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    