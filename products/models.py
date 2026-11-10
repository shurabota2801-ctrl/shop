from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:products_list_with_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Категория')
    name =  models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(max_length=5000, blank=True, verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Обновлено')
    created = models.DateTimeField(auto_now=True, verbose_name='Создано')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])



