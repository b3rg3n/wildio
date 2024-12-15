from django.shortcuts import render
from .models import Game

def check_games(request):
    games = Game.objects.all()
    return render(request, 'games/games.html', {'games': games})