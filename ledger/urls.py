from django.urls import path
from .views import BalanceView, DepositView, TransactionHistoryView

urlpatterns = [
    path('accounts/<int:id>/balance/', BalanceView.as_view()),
    path('deposit/', DepositView.as_view()),
    path('transactions/', TransactionHistoryView.as_view()),
]