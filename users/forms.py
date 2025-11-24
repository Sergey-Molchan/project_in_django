from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django.core.exceptions import ValidationError


class UsersRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите ваш email'
        }),
        help_text="Обязательное поле. Введите действующий email адрес."
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
        help_text="""
        <ul class="form-text">
            <li>Пароль не должен быть слишком похож на другую вашу личную информацию.</li>
            <li>Пароль должен содержать как минимум 8 символов.</li>
            <li>Пароль не должен быть слишком простым и распространенным.</li>
            <li>Пароль не может состоять только из цифр.</li>
        </ul>
        """
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повторите пароль'
        }),
        help_text="Для подтверждения введите, пожалуйста, пароль ещё раз."
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Удаляем поле username из формы
        if 'username' in self.fields:
            del self.fields['username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")
        return email