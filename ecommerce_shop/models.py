from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название категории")
    slug = models.SlugField(verbose_name="Слаг категории")

    def get_absolute_url(self):
        return reverse('catalog_deep', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    slug = models.SlugField(verbose_name="Слаг продукта", unique=True)
    title = models.CharField(max_length=150, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта")
    image = models.ImageField(verbose_name="Изображение")
    price = models.FloatField(verbose_name="Цена продукта", default=0)
    discount = models.FloatField(verbose_name="Скидка", blank=True, null=True)
    draft = models.BooleanField(verbose_name="Черновик", default=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.category.slug, 'product_slug': self.slug})

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return str(self.title)
