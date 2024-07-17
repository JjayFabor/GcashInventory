from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import uuid


# Investment Model
class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.total_amount}"

    def update_total(self, transaction_type, amount, fee, reverse=False):
        if transaction_type == "Cash In":
            if reverse:
                self.total_amount -= amount + fee
            else:
                self.total_amount += amount + fee
        elif transaction_type == "Cash Out":
            if reverse:
                self.total_amount += amount
                self.total_amount -= fee
            else:
                self.total_amount -= amount
                self.total_amount += fee
        self.save()


# Transaction Model
class Transaction(models.Model):
    DEPOSIT = "Cash In"
    WITHDRAWAL = "Cash Out"

    TRANSACTION_TYPES_CHOICES = [(DEPOSIT, "Cash In"), (WITHDRAWAL, "Cash Out")]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(
        max_length=10, choices=TRANSACTION_TYPES_CHOICES, default=DEPOSIT
    )
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # description = models.TextField(blank=True, null=True)
    description = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} of {self.amount}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.investment.update_total(self.transaction_type, self.amount, self.fee)
