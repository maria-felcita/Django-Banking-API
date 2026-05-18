from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Account
from .serializers import AccountSerializer
from rest_framework.exceptions import ValidationError

class AccountListCreateView(ListCreateAPIView):
    serializer_class = AccountSerializer  
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):  
        user = self.request.user  

        if user.role == 'admin':  
            return Account.objects.all()  

        return Account.objects.filter(user=user)  

    def perform_create(self, serializer):  

        if Account.objects.filter(user=self.request.user).exists():  
            raise ValidationError("User already has an account")  

        serializer.save(user=self.request.user)  