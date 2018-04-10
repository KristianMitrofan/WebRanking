from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length = 100)
    ranking = models.IntegerField(default= 22)
    performances = models.IntegerField(default= 0)

    def __str__(self):
        return self.name + " : " + str(self.ranking) + " : " + str(self.performances)

class Match(models.Model):
    winner = models.CharField(max_length = 100)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.winner