from rest_framework import serializers

class TransferSerializer(serializers.Serializer):
    to_account_id = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    idempotency_key = serializers.CharField()