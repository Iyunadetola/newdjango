from django.contrib import admin

# Register your models here.

from .models import *

class Applicantadmin(admin.ModelAdmin):

    list_display=('firstname', 'lastname', 'email', 'phone', 'amount', 'address', 'course', 'center', 'mode')

    list_filter=('firstname', 'lastname', 'address', 'course', 'center', 'date')

admin.site.register(Applicants, Applicantadmin)
