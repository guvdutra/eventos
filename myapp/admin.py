from django.contrib import admin
from .models import Evento, Participante

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'horario', 'local')
    search_fields = ('nome', 'descricao')

@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
