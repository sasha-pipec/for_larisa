# Generated by Django 4.2 on 2023-05-01 12:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanApp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Колличесвто')),
                ('in_order', models.BooleanField(default=False, verbose_name='В заказе')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanApp.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Элемент корзины',
                'verbose_name_plural': 'Элементы корзины',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, verbose_name='Отзыв')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanApp.product', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=100, verbose_name='Номер заказа')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('shopping_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sanApp.shoppingcard', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]