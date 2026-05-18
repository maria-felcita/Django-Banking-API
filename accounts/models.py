from django.db import models
from django.conf import settings
import uuid

# Create your models here.
class Account(models.Model):
    STATUS_CHOICES = [  
        ('active', 'Active'),  
        ('frozen', 'Frozen')  
    ]  

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  
    account_number = models.CharField(max_length=20, unique=True, default=uuid.uuid4)  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):  
        return str(self.account_number)  