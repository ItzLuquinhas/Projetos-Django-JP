from django.contrib import admin
from .models import Carro


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'cidade', 'destaque')
    list_filter = ('marca', 'destaque')
    search_fields = ('marca', 'modelo')