from django.contrib import admin
from .models import Card

# Register your models here.
class CardAdmin(admin.ModelAdmin):
    fields = ('title', 'pages_used', 'short_description')
    list_display = ['title', 'pages_used', 'short_description']
    search_fields = ['title']
    list_filter = ['title']
    list_editable = ['pages_used', 'short_description']

admin.site.register(Card, CardAdmin)