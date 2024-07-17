from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_view, name="gcash-home"),
    path("add-investment/", views.addInvestmentView, name="add-investment"),
    path("view-transaction/", views.view_transaction, name="view-transaction"),
    path(
        "delete-transaction/<int:id>/",
        views.delete_transaction,
        name="delete-transaction",
    ),
    path("logout/", views.logout_view, name="logout"),
]
