from django.db import models
from accounts.models import Account

# Create your models here.
class LedgerEntry(models.Model):
    ENTRY_TYPE = [  
        ('debit', 'Debit'),  
        ('credit', 'Credit')  
    ]  

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='entries')  
    amount = models.DecimalField(max_digits=12, decimal_places=2)  
    entry_type = models.CharField(max_length=10, choices=ENTRY_TYPE)  
    reference_id = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True)  

    class Meta:  
        indexes = [  
            models.Index(fields=['account', 'created_at'])  
        ]  