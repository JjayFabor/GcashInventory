from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Investment, Transaction
from .serializer import InvestmentSerializer, TransactionSerializer
from . import forms
from rest_framework import viewsets
from rest_framework.response import Response


@login_required
def addInvestmentView(request):
    # Check if the user has already investment
    if Investment.objects.filter(user=request.user).exists():
        return redirect("gcash-home")

    if request.method == "POST":
        form = forms.AddInvestment(request.POST, request.FILES)
        if form.is_valid():
            newInvestment = form.save(commit=False)
            newInvestment.user = request.user
            newInvestment.save()
            return redirect("gcash-home")
    else:
        form = forms.AddInvestment()

    return render(request, "add_investment.html", {"show_navbar": True, "form": form})


@login_required
def home_view(request):
    investment = Investment.objects.filter(user=request.user)
    if request.method == "POST":
        form = forms.AddTransaction(request.POST, request.FILES)
        if form.is_valid():
            newTransaction = form.save(commit=False)
            newTransaction.user = request.user
            if investment.exists():
                newTransaction.investment = investment.first()
            newTransaction.save()
            return redirect("view-transaction")
    else:
        form = forms.AddTransaction()
    return render(
        request,
        "home.html",
        {"form": form, "show_navbar": True, "investments": investment},
    )


@login_required
def view_transaction(request):
    transactions = Transaction.objects.filter(user=request.user)
    return render(
        request,
        "view_transaction.html",
        {"transactions": transactions, "show_navbar": True},
    )


@login_required
def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    if request.method == "POST":
        # Reverse the transaction for the investment
        investment = transaction.investment
        investment.update_total(
            transaction.transaction_type,
            transaction.amount,
            transaction.fee,
            reverse=True,
        )

        transaction.delete()
        return redirect("view-transaction")


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")


# class InvestmentViewSet(viewsets.ModelViewSet):
#     queryset = Investment.objects.all()
#     serializer_class = InvestmentSerializer


# class TransactionViewSet(viewsets.ModelViewSet):
#     queryset = Transaction.objects.all()
#     serializer_class = TransactionSerializer
