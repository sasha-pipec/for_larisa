from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to="images/%Y/%m/%d/", verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f"{self.name} - {self.price}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Review(models.Model):
    comment = models.CharField(max_length=255, verbose_name='Отзыв')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class ShoppingCard(models.Model):
    quantity = models.IntegerField(verbose_name='Колличесвто')
    in_order = models.BooleanField(default=False, verbose_name='В заказе')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'Элемент корзины'
        verbose_name_plural = 'Элементы корзины'


class Order(models.Model):
    order_number = models.CharField(max_length=100, verbose_name='Номер заказа')
    shopping_card = models.ForeignKey('ShoppingCard', on_delete=models.CASCADE, verbose_name='Товар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
