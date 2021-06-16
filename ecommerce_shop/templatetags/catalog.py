from django import template
from ecommerce_shop.models import Category

register = template.Library()


@register.simple_tag
def catalog():
    return Category.objects.all()
