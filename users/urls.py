from django.contrib.auth.views import LoginView, LogoutView
from users.apps import UsersConfig
from django.urls import path
from users.views import UserCreateView, email_verification, EmailVerificationSentView, ProfileUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('email-verification-sent/', EmailVerificationSentView.as_view(), name='email_verification_sent'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
]
