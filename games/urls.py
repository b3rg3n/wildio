from django.urls import path

from . import views

urlpatterns = [
    path("games/all/", views.check_games),
]