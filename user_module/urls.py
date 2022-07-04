from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path('register/', views.Registration.as_view(), name='register'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('forgotpassword/', views.ForgotPassword.as_view(), name='login'),
    path('resetpassword/<uid>/<token>/', views.ResetPassword.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='login'),
]
