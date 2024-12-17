from rest_framework import serializers
from .models import Game, GameHistory, Promocode

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'name', 'description', 'image', 'status']

class GameHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GameHistory
        fields = ['id', 'result', 'game', 'user']

class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ['id', 'name', 'cofficient']