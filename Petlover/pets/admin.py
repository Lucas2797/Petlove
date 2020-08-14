from django.contrib import admin
from .models import Pets, People

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('user', 'birthday', 'cpf')

class PetsAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'nome', 'custo', 'tipo')


admin.site.register(Pets, PetsAdmin),
admin.site.register(People, PeopleAdmin),


