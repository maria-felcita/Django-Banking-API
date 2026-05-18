from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.models import Account
from .services import get_balance
from .serializers import BalanceSerializer, DepositSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied, ValidationError
from .models import LedgerEntry
import uuid
from rest_framework.generics import ListAPIView
from .serializers import LedgerEntrySerializer
from rest_framework.exceptions import ValidationError
from .pagination import LedgerPagination

# Create your views here.
class BalanceView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]  
    queryset = Account.objects.all()  
    lookup_field = 'id'  
    serializer_class = BalanceSerializer  

    def retrieve(self, request, *args, **kwargs):  

        account = self.get_object()  

        if request.user.role != 'admin' and account.user != request.user:  
            from rest_framework.exceptions import PermissionDenied  
            raise PermissionDenied("Not your account")  

        bal = get_balance(account.id)  

        return Response({  
            "account_id": account.id,  
            "balance": bal  
        })  
    

class DepositView(APIView):
    permission_classes = [IsAuthenticated]  

    def post(self, request):  

        serializer = DepositSerializer(data=request.data)  
        serializer.is_valid(raise_exception=True)  

        amount = serializer.validated_data['amount']  

        account = Account.objects.filter(user=request.user).first()  

        if not account:  
            raise ValidationError("User has no account")  

        LedgerEntry.objects.create(  
            account=account,  
            amount=amount,  
            entry_type='credit',  
            reference_id=str(uuid.uuid4())  
        )  

        return Response({  
            "message": "Deposit successful"  
        })
    

class TransactionHistoryView(ListAPIView):

    serializer_class = LedgerEntrySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = LedgerPagination

    def get_queryset(self):

        account = Account.objects.filter(user=self.request.user).first()

        if not account:
            raise ValidationError("User has no account")

        qs = LedgerEntry.objects.filter(account=account).order_by('-created_at')

        entry_type = self.request.query_params.get('type')

        if entry_type:
            qs = qs.filter(entry_type=entry_type)

        return qs