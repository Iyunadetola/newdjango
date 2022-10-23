from django.contrib import admin

# Register your models here.

from .models import *

class ShopAdmin(admin.ModelAdmin):
    list_display=('name', 'description', 'date', 'price', 'image')
    list_filter=('name','date', 'price')

admin.site.register(Shop, ShopAdmin)
