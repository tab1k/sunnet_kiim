from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    last_price = models.PositiveIntegerField(default=0, blank=True, null=True)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discount = models.IntegerField(default=0, blank=True, null=True)
    is_have = models.BooleanField(default=True, blank=True, null=True)
    category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


