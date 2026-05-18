from django.urls import path
from .views import RegisterView, ProfileView, AllUsersView, ManagerDashboardView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('admin/users/', AllUsersView.as_view()),
    path('manager/dashboard/', ManagerDashboardView.as_view()),
]