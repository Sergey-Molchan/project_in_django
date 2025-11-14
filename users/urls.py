from django.contrib.auth.views import LoginView
from users.apps import UsersConfig
from django.urls import path

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login/html'))
]