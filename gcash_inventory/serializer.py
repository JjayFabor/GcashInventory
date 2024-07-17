from rest_framework import serializers
from .models import Transaction, Investment


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ["id", "user", "total_amount", "update_at"]


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "user",
            "transaction_type",
            "investment",
            "amount",
            "fee",
            "description",
            "date",
            "transaction_id",
        ]
