from django.contrib import admin

from .models import Menu, Restaurant


admin.site.register(Restaurant)
admin.site.register(Menu)