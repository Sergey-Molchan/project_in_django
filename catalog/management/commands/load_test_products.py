from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        from catalog.models import Product, Category, Contact

        # Удаляем старые данные
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        Contact.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(' Старые данные удалены'))

        # Загружаем фикстуры
        self.stdout.write(' Загрузка фикстур...')

        fixtures = ['category.json', 'product.json', 'contact.json']

        for fixture in fixtures:
            try:
                call_command('loaddata', fixture)
                self.stdout.write(f' Загружено: {fixture}')
            except Exception as e:
                self.stdout.write(self.style.ERROR(f' Ошибка загрузки {fixture}: {e}'))

        self.stdout.write(self.style.SUCCESS('🎉 Все тестовые данные загружены!'))