from django.contrib import admin
from .models import player
# Register your models here.

@admin.register(player)
class Player_admin(admin.ModelAdmin):
	list_display=('jugador1','jugador2','jugador3',)
	list_filter=('jugador1', )
	search_fields=('jugador1','jugador2','jugador3')
