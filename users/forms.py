from django.contrib.auth.forms import UserCreationForm
from users.models import User
from catalog.models import StyleFormMixin



class UsersRegisterForm(StyleFormMixin, UserCreationForm):
    model = User
    fields = ['email', "password1", 'password2']