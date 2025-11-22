from django import template

register = template.Library()

@register.filter
def can_edit_product(user, product):
    """Может ли пользователь редактировать продукт"""
    return product.owner == user

@register.filter
def can_delete_product(user, product):
    """Может ли пользователь удалить продукт"""
    if product.owner == user:
        return True
    return user.has_perm('catalog.delete_product')

@register.filter
def can_unpublish_product(user):
    """Может ли пользователь отменять публикацию"""
    return user.has_perm('catalog.can_unpublish_product')