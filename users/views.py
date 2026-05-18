from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdmin, IsManager

# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()  
    serializer_class = RegisterSerializer  
    permission_classes = [AllowAny]

class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):  
        return Response({  
            "username": request.user.username,  
            "role": request.user.role  
        })

class AllUsersView(ListAPIView):
    queryset = User.objects.all()  
    serializer_class = RegisterSerializer  
    permission_classes = [IsAdmin]


class ManagerDashboardView(APIView):
    permission_classes = [IsManager]
    # User.  
    def get(self, request):
        return Response({
            "message": "Manager or Admin access granted"
            })