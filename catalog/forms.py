import os
from django.core.files.images import get_image_dimensions
from django import forms
from django.core.exceptions import ValidationError
from .models import Product  # ⬅️ Импортируем из catalog!


class ProductForm(forms.ModelForm):
    # Запрещенные слова из задания
    FORBIDDEN_WORDS = [
        'казино', 'криптовалюта', 'крипта', 'биржа',
        'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_name(self):
        """Валидация названия на запрещенные слова"""
        name = self.cleaned_data['name']
        return self._validate_no_forbidden_words(name, 'названии')

    def clean_description(self):
        """Валидация описания на запрещенные слова"""
        description = self.cleaned_data.get('description', '')
        return self._validate_no_forbidden_words(description, 'описании')

    def clean_price(self):
        """Валидация цены - не может быть отрицательной"""
        price = self.cleaned_data['price']
        if price < 0:
            raise ValidationError('Цена не может быть отрицательной')
        return price

    def _validate_no_forbidden_words(self, text, field_name):
        """Общий метод проверки на запрещенные слова"""
        if text:
            text_lower = text.lower()
            for word in self.FORBIDDEN_WORDS:
                if word in text_lower:
                    raise ValidationError(
                        f'Запрещенное слово "{word}" в {field_name} продукта'
                    )
        return text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Стилизация всех полей
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'image':
                field.widget.attrs['class'] = 'form-control-file'


    def clean_image(self):
        image = self.cleaned_data.get('image')

        if image:
            # Проверка формата
            valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
            ext = os.path.splitext(image.name)[1].lower()
            if ext not in valid_extensions:
                raise ValidationError(
                    'Поддерживаются только следующие форматы: JPG, JPEG, PNG, WEBP'
                )

            # Проверка размера файла (5 МБ)
            if image.size > 5 * 1024 * 1024:
                raise ValidationError('Размер файла не должен превышать 5 МБ')


            try:
                width, height = get_image_dimensions(image)
                if not width or not height:
                    raise ValidationError('Невозможно определить размеры изображения')
            except Exception:
                raise ValidationError('Файл не является корректным изображением')

        return image