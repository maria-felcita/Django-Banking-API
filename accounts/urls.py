from django.urls import path
from .views import AccountListCreateView

urlpatterns = [
    path('accounts/', AccountListCreateView.as_view()),
]