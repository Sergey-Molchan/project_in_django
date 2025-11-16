from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from users.forms import UsersRegisterForm
from users.models import User
import secrets
from config.settings import EMAIL_HOST_USER


class UserCreateView(CreateView):
    model = User
    form_class = UsersRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        host = self.request.get_host()
        url = f'http://{host}/users.email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f"Здравствуйте! спасибо что зарегистрировались в нашем магазине. Перейдите по ссылке для окончания регистрации {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(requests, token):
    user = User.get_object_or_404(User, token=token)
    User.is_active = True
    return redirect(reverse('users:login'))