from django.core.management.base import BaseCommand
from django.utils import timezone
from catalog.models import Category, Product
from django.db import models


class Command(BaseCommand):
    help = 'Загружает тестовые продукты (удаляет существующие данные перед добавлением)'

    def handle(self, *args, **options):
        # Удаляем все существующие данные
        self.stdout.write('🗑️ Удаление существующих продуктов и категорий...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('✅ Существующие данные удалены'))

        # Создаем категории
        self.stdout.write('📁 Создание категорий...')
        categories_data = [
            {'name': 'Электроника', 'description': 'Современные электронные устройства и гаджеты'},
            {'name': 'Одежда', 'description': 'Модная одежда и аксессуары для всех возрастов'},
            {'name': 'Книги', 'description': 'Художественная и образовательная литература'},
            {'name': 'Дом и сад', 'description': 'Товары для дома, сада и ремонта'},
            {'name': 'Спорт', 'description': 'Спортивные товары и инвентарь'},
            {'name': 'Красота и здоровье', 'description': 'Косметика, парфюмерия и товары для здоровья'},
        ]

        categories = {}
        for cat_data in categories_data:
            category = Category.objects.create(
                name=cat_data['name'],
                description=cat_data['description']
            )
            categories[cat_data['name']] = category
            self.stdout.write(f'✅ Создана категория: {cat_data["name"]}')

        # Создаем продукты
        self.stdout.write('📦 Создание продуктов...')
        products_data = [
            {
                'name': 'Смартфон Samsung Galaxy S23',
                'description': 'Флагманский смартфон с мощным процессором и отличной камерой',
                'price': 79999.99,
                'category': 'Электроника'
            },
            {
                'name': 'Ноутбук ASUS VivoBook 15',
                'description': 'Стильный и производительный ноутбук для работы и учебы',
                'price': 54999.50,
                'category': 'Электроника'
            },
            {
                'name': 'Наушники Sony WH-1000XM4',
                'description': 'Беспроводные наушники с шумоподавлением',
                'price': 29999.00,
                'category': 'Электроника'
            },
            {
                'name': 'Джинсы классические',
                'description': 'Удобные джинсы прямого кроя из качественного денима',
                'price': 2999.00,
                'category': 'Одежда'
            },
            {
                'name': 'Футболка хлопковая',
                'description': 'Мягкая футболка из 100% хлопка, различные цвета',
                'price': 1499.00,
                'category': 'Одежда'
            },
            {
                'name': 'Куртка зимняя',
                'description': 'Теплая куртка для холодной погоды',
                'price': 7999.00,
                'category': 'Одежда'
            },
            {
                'name': 'Мастер и Маргарита',
                'description': 'Роман Михаила Булгакова - классика русской литературы',
                'price': 599.00,
                'category': 'Книги'
            },
            {
                'name': 'Python для начинающих',
                'description': 'Подробный учебник по программированию на Python с примерами',
                'price': 1299.00,
                'category': 'Книги'
            },
            {
                'name': 'Атлас мира',
                'description': 'Подробный географический атлас с картами стран',
                'price': 1999.00,
                'category': 'Книги'
            },
            {
                'name': 'Кофемашина DeLonghi',
                'description': 'Автоматическая кофемашина для приготовления эспрессо и капучино',
                'price': 45999.00,
                'category': 'Дом и сад'
            },
        ]

        for prod_data in products_data:
            product = Product.objects.create(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                category=categories[prod_data['category']]
            )
            self.stdout.write(f'✅ Создан продукт: {prod_data["name"]}')

        self.stdout.write(
            self.style.SUCCESS(f'🎉 Успешно создано: {Category.objects.count()} категорий и {Product.objects.count()} продуктов')
        )