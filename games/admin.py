from django.contrib import admin
from .models import Game, GameHistory, Promocode

admin.site.register(Game)
admin.site.register(GameHistory)
admin.site.register(Promocode)