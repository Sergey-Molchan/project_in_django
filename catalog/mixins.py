from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class OwnerRequiredMixin(UserPassesTestMixin):
    """Миксин для проверки, что пользователь - владелец объекта"""

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        obj = self.get_object()
        return obj.owner == self.request.user


class ModeratorRequiredMixin(UserPassesTestMixin):
    """Миксин для проверки прав модератора"""

    def test_func(self):
        return self.request.user.has_perm('catalog.can_unpublish_product')


class OwnerOrModeratorMixin(UserPassesTestMixin):
    """Миксин для проверки владельца или модератора"""

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False

        obj = self.get_object()
        user = self.request.user


        if obj.owner == user:
            return True


        if user.has_perm('catalog.can_unpublish_product'):
            return True

        return False


