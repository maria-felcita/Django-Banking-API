from django.db.models import Sum
from .models import LedgerEntry

def get_balance(account_id):
    credit = LedgerEntry.objects.filter(  
        account_id=account_id,  
        entry_type='credit'  
    ).aggregate(Sum('amount'))['amount__sum'] or 0  

    debit = LedgerEntry.objects.filter(  
        account_id=account_id,  
        entry_type='debit'  
    ).aggregate(Sum('amount'))['amount__sum'] or 0  

    return credit - debit  