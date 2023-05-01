from django.contrib import admin

# Register your models here.
from sanApp.models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('comment',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
