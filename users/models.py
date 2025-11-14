from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class User(AbstractUser):
    username = None
    email = models.EmailField(unique= True, verbose_name='Email')
    phone_number = PhoneNumberField(blank=True, verbose_name='Телефон', help_text='Введите номер телефона')
    tg_name = models.CharField(max_length=50, verbose_name='Telegram', blank=True, null=True, help_text='Введите ваш телеграм ник')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватарка', help_text='Загрузите фото профиля')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email