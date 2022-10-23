from django.contrib import admin

# Register your models here.

from .models import *

class MyContactadmin(admin.ModelAdmin):

    list_display=('name', 'email', 'subjectmatter', 'phonenumber', 'message')

    list_filter=('name', 'email', 'subjectmatter', 'phonenumber', 'message')

admin.site.register(MyContact, MyContactadmin)