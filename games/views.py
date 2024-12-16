from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema

from .models import Game, GameHistory
from django.http import JsonResponse
from rest_framework import generics
from .serializers import GameSerializer, GameHistorySerializer


class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @swagger_auto_schema(
        operation_description="Получить список игр или создать новую игру",
        responses={200: GameSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новую игру",
        request_body=GameSerializer,
        responses={201: GameSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class GameHistoryListCreate(generics.ListCreateAPIView):
    queryset = GameHistory.objects.all()
    serializer_class = GameHistorySerializer

    @swagger_auto_schema(
        operation_description="Получить список всех историй игр",
        responses={200: GameHistorySerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новую историю игр",
        request_body=GameSerializer,
        responses={201: GameHistorySerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# def check_games(request):
#     games = list(Game.objects.values('id', 'name', 'description', 'image', 'status'))
#     return JsonResponse({'games': games})
#
# def history_games(request):
#     historygames = list(GameHistory.objects.values('id', 'result', 'game', 'user'))
#     return JsonResponse({'historygames': historygames})
