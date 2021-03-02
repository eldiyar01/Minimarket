from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryModel(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductModel(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryModel(admin.ModelAdmin):
    pass
