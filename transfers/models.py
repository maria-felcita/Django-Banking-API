from django.db import models
from accounts.models import Account

class Transfer(models.Model):

    idempotency_key = models.CharField(max_length=100, unique=True)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sent')
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='received')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, default='success')
    created_at = models.DateTimeField(auto_now_add=True)