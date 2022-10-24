from django.contrib import admin

# Register your models here.
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    fields = ('nome', 'slug', 'imagem', 'valor', 'desconto')
    list_display = ['nome', 'slug', 'imagem', 'valor', 'desconto']
    search_fields = ['nome', 'imagem']
    list_filter = ['valor']
    list_editable = ['slug', 'imagem', 'valor', 'desconto']
    prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Produto, ProdutoAdmin)