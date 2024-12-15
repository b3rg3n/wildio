from django.db import models

from userauth.models import User


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class GameHistory(models.Model):
    id = models.AutoField(primary_key=True)
    result = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def shared_property(self):
        return self.user.username

    class Meta:
        verbose_name = 'История игр'
        verbose_name_plural = 'Истории игр'

class Promocode(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    cofficient = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'