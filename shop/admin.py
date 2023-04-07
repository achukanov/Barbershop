from django.contrib import admin

from .models import *
from telebot.models import *

class ImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 4
    extra = 4

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'producer', 'created_at', 'updated_at', 'on_sale',
                    'units_price', 'units_in_stock', 'article')
    list_display_links = ('id', 'product_name', 'category', 'producer', 'article')
    search_fields = ('product_name', 'content')
    list_editable = ('on_sale',)
    list_filter = ('on_sale', 'category')
    sortable_by = ('id')
    inlines = [ImageInline]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', )
    sortable_by = ('id')
    prepopulated_fields = {"slug": ("title",)}

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title', )
    sortable_by = ('id')
    prepopulated_fields = {"slug": ("title",)}






admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Producer, ProducerAdmin)
# admin.site.register(ProductImage, ImageAdmin)
