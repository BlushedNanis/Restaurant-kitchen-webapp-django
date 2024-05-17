from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "price", "status", "author")
    list_filter = ("status", "author", "meal_type")
    search_fields = ("meal", "description")
    
    
admin.site.register(Item, MenuItemAdmin)