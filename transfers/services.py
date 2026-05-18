from django.db import transaction
from rest_framework.exceptions import ValidationError
from accounts.models import Account
from ledger.models import LedgerEntry
from ledger.services import get_balance
from .models import Transfer
import uuid

def transfer_funds(user, to_account_id, amount, idempotency_key):

    existing = Transfer.objects.filter(idempotency_key=idempotency_key).first()
    if existing:
        return existing

    from_account = Account.objects.filter(user=user).first()
    if not from_account:
        raise ValidationError("Sender account not found")

    with transaction.atomic():

        accounts = Account.objects.select_for_update().filter(
            id__in=[from_account.id, to_account_id]
        )

        if accounts.count() != 2:
            raise ValidationError("Invalid receiver account")

        sender = accounts.get(id=from_account.id)
        receiver = accounts.get(id=to_account_id)

        balance = get_balance(sender.id)

        if balance < amount:
            raise ValidationError("Insufficient balance")

        ref = str(uuid.uuid4())

        LedgerEntry.objects.create(
            account=sender,
            amount=amount,
            entry_type='debit',
            reference_id=ref
        )

        LedgerEntry.objects.create(
            account=receiver,
            amount=amount,
            entry_type='credit',
            reference_id=ref
        )

        transfer = Transfer.objects.create(
            idempotency_key=idempotency_key,
            from_account=sender,
            to_account=receiver,
            amount=amount
        )

        return transfer