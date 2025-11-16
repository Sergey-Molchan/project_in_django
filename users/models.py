# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid


class User(AbstractUser):
    DoesNotExist = None
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone_number = PhoneNumberField(blank=True, verbose_name='Телефон', help_text='Введите номер телефона')
    tg_name = models.CharField(max_length=50, verbose_name='Telegram', blank=True, null=True,
                               help_text='Введите ваш телеграм ник')
    avatar = models.ImageField(upload_to='users/avatars', blank=True, null=True, verbose_name='Аватарка',
                               help_text='Загрузите фото профиля')
    token = models.CharField(max_length=100, verbose_name='Token', blank=True, null=True)

    # Поля для верификации
    email_verified = models.BooleanField(default=False, verbose_name='Email подтвержден')
    is_active = models.BooleanField(default=False, verbose_name='Активный')  # По умолчанию неактивен

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'

    def save(self, *args, **kwargs):
        # Автоматически генерируем token при создании пользователя
        if not self.token:
            self.token = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email