from django.contrib import admin
from .models import Membro

# admin.site.register(Membro)

@admin.register(Membro)
class MembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'curso', 'matricula', 'email')