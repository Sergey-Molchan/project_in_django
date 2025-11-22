from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Получаем контент-тайп для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Создаем группу "Модератор продуктов"
        moderators_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Добавляем права для модераторов
        moderator_permissions = [
            'can_unpublish_product',
            'delete_product',  # Удаление любого продукта
            'view_product',  # Просмотр продуктов
            'change_product',  # Изменение продуктов
        ]

        for perm_codename in moderator_permissions:
            if perm_codename.startswith('can_'):
                # Кастомные права
                permission, created = Permission.objects.get_or_create(
                    codename=perm_codename,
                    content_type=content_type,
                    defaults={'name': perm_codename}
                )
            else:
                # Стандартные права Django
                permission = Permission.objects.get(
                    codename=perm_codename,
                    content_type=content_type
                )
            moderators_group.permissions.add(permission)

        # Создаем группу "Контент-менеджер" (дополнительное задание)
        content_managers_group, created = Group.objects.get_or_create(name='Контент-менеджер')

        # Права для контент-менеджеров (работа с блогом)
        blog_content_type = ContentType.objects.get(app_label='blog', model='article')
        content_manager_permissions = Permission.objects.filter(
            content_type=blog_content_type
        )
        for perm in content_manager_permissions:
            content_managers_group.permissions.add(perm)

        self.stdout.write(
            self.style.SUCCESS('Группы и права успешно созданы!')
        )
