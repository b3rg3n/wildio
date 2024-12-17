from django.shortcuts import render, get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, GameHistory, Promocode
from django.http import JsonResponse
from rest_framework import generics
from .serializers import GameSerializer, GameHistorySerializer, PromocodeSerializer

class GameDetailView(APIView):
    def get(self, request, id, format=None):
        try:
            game = Game.objects.get(id=id)
        except Game.DoesNotExist:
            raise NotFound(detail="Game not found")

        serializer = GameSerializer(game)
        return Response(serializer.data)

class GameListCreate(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    #game_once = Game.objects.get(id=id)

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
         request_body=GameHistorySerializer,
         responses={201: GameHistorySerializer}
    )
    def post(self, request, *args, **kwargs):
         return super().post(request, *args, **kwargs)

class PromocodeListCreate(generics.ListCreateAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer

    @swagger_auto_schema(
        operation_description="Получить список всех промокодов",
        responses={200: PromocodeSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создать новый промокод",
        request_body=PromocodeSerializer,
        responses={201: PromocodeSerializer}
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
