from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TransferSerializer
from .services import transfer_funds

class TransferView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = TransferSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        transfer = transfer_funds(
            request.user,
            data['to_account_id'],
            data['amount'],
            data['idempotency_key']
        )

        return Response({
            "transfer_id": transfer.id,
            "status": transfer.status
        })