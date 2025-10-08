# 🛍️ iShop - Интернет-магазин

![Django](https://img.shields.io/badge/Django-4.2.7-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple)
![Python](https://img.shields.io/badge/Python-3.13-blue)

Современный интернет-магазин, разработанный на Django с использованием Bootstrap 5.

## 📋 О проекте

iShop - это полнофункциональный интернет-магазин с современным дизайном и адаптивной версткой. Проект создан в рамках учебного курса по Django и постоянно развивается.

### 🌟 Основные возможности

- ✅ **Главная страница** с приветственным разделом и категориями товаров
- ✅ **Страница контактов** с формой обратной связи
- ✅ **Адаптивный дизайн** - корректное отображение на всех устройствах
- ✅ **Современный UI** с использованием Bootstrap 5
- ✅ **Навигация** между страницами

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8+
- pip (менеджер пакетов Python)
- Git

### Установка и запуск

1. **Клонируйте репозиторий**

git clone https://github.com/Sergey-Molchan/project_in_django.git
cd project_in_django
Создайте виртуальное окружение

python -m venv venv
source venv/bin/activate  # Linux/MacOS
# или
venv\Scripts\activate     # Windows
Установите зависимости

pip install -r requirements.txt
Примените миграции

python manage.py migrate
Запустите сервер разработки

python manage.py runserver
Откройте в браузере
text
http://127.0.0.1:8000/
📁 Структура проекта

text
project_in_django/
├── config/                 # Настройки Django проекта
│   ├── settings.py        # Основные настройки
│   ├── urls.py           # Главные URL-маршруты
│   └── wsgi.py           # WSGI конфигурация
├── catalog/               # Приложение каталога
│   ├── migrations/       # Миграции базы данных
│   ├── templates/        # HTML шаблоны
│   │   └── catalog/
│   │       ├── home.html      # Главная страница
│   │       └── contacts.html  # Страница контактов
│   ├── admin.py         # Админ-панель
│   ├── apps.py          # Конфигурация приложения
│   ├── models.py        # Модели данных
│   ├── tests.py         # Тесты
│   ├── urls.py          # URL-маршруты приложения
│   └── views.py         # Контроллеры (views)
├── static/              # Статические файлы (CSS, JS, изображения)
├── media/               # Медиафайлы (загружаемые пользователями)
├── requirements.txt     # Зависимости проекта
├── manage.py           # Утилита управления Django
└── README.md           # Этот файл