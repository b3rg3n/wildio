from django.shortcuts import render
from .models import Game
from django.http import JsonResponse

def check_games(request):
    games = list(Game.objects.values('id', 'name', 'description', 'image', 'status'))
    return JsonResponse({'games': games})