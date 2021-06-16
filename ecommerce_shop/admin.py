from django.contrib import admin
from ecommerce_shop.models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ("Название", {
            "fields": (("title", "slug"), ("description",))
        }),
        ("Управление", {
            "fields": ("draft", "category", "image")
        }),
        ("Цена", {
            "fields": ("price", "discount")
        }),

    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
