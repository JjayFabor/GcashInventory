from django import forms
from . import models


class AddInvestment(forms.ModelForm):
    class Meta:
        model = models.Investment
        fields = ["total_amount"]


class AddTransaction(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ["transaction_type", "amount", "fee", "description"]
