from django.contrib import admin
from .models import Pessoa

class ListaPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 3

admin.site.register(Pessoa, ListaPessoas)
