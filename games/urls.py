from django.urls import path

from . import views
from .views import GameListCreate, GameHistoryListCreate

urlpatterns = [
    path('all/', GameListCreate.as_view(), name='game-list-create'),
    path('history/', GameHistoryListCreate.as_view(), name='gamehistory-list-create'),

    #path("all/", views.check_games, name="games_all"),
    #path("history/", views.history_games, name="games_history"),
]