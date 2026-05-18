from rest_framework import serializers
from .models import LedgerEntry

class BalanceSerializer(serializers.Serializer):
    account_id = serializers.IntegerField()
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)


class DepositSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)


class LedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerEntry
        fields = (
            'id',
            'amount',
            'entry_type',
            'reference_id',
            'created_at'
        )