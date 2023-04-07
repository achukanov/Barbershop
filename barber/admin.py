from django.contrib import admin

from .models import *
from telebot.models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at', 'updated_at', 'is_published')
    # list_display_links = ('id',)
    # search_fields = ('content',)
    list_editable = ('is_published',)
    sortable_by = ('is_published', )

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'name', 'phone', 'confirmed', 'performed', 'сancel', 'created_at',)
    list_display_links = ('id', 'date', 'time', 'name', 'phone')
    search_fields = ('name', 'phone')
    list_editable = ('confirmed', 'performed', 'сancel')
    list_filter = ('confirmed', 'performed', 'сancel')


admin.site.register(News, NewsAdmin)
admin.site.register(Booking, BookingAdmin)
