from django.contrib import admin
from .models import Properties


class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ["realtor", 'is_published']
    list_editable = ('is_published',)
    search_fields = ['title', 'description', 'address', 'state', 'city', 'zipcode', 'price']
    list_per_page = 25


admin.site.register(Properties, PropertiesAdmin)

