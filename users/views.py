from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from .forms import UsersRegisterForm
from .models import User


class UserCreateView(CreateView):
    model = User
    form_class = UsersRegisterForm
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        # Сохраняем пользователя как НЕактивного
        self.object = form.save(commit=False)
        self.object.is_active = False  # Блокируем доступ до верификации
        # Token автоматически создается в методе save() модели
        self.object.save()

        # Отправляем email с ссылкой для верификации
        try:
            verification_url = self.request.build_absolute_uri(
                reverse('users:email-confirm', kwargs={'token': self.object.token})
            )

            send_mail(
                subject='Подтверждение email в нашем магазине',
                message=f'''Здравствуйте, {self.object.email}!

Для завершения регистрации подтвердите ваш email, перейдя по ссылке:
{verification_url}

Ссылка действительна всегда.

Если вы не регистрировались в нашем магазине, проигнорируйте это письмо.

С уважением,
Команда магазина''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.object.email],
                fail_silently=False,
            )
            # Перенаправляем на страницу "письмо отправлено"
            return redirect('users:email_verification_sent')

        except Exception as e:
            # Если email не отправился, удаляем пользователя
            self.object.delete()
            messages.error(self.request, f'Ошибка при отправке email: {str(e)}')
            return self.form_invalid(form)

    def get_success_url(self):
        # Этот метод больше не используется, так как мы делаем redirect в form_valid
        return reverse_lazy('users:email_verification_sent')


class EmailVerificationSentView(TemplateView):
    template_name = 'users/email_verification_sent.html'


def email_verification(request, token):
    try:
        user = get_object_or_404(User, token=token)
        if not user.email_verified:
            user.email_verified = True
            user.is_active = True  # Активируем после верификации
            user.save()
            messages.success(request, '✅ Ваш email успешно подтвержден! Теперь вы можете войти в систему.')
        else:
            messages.info(request, '✅ Ваш email уже подтвержден.')
    except User.DoesNotExist:
        messages.error(request, '❌ Неверная или устаревшая ссылка подтверждения.')

    return redirect('users:login')