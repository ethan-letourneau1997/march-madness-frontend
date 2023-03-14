from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here. d


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    draft_active = models.BooleanField(default=True)
    draft_order = ArrayField(models.IntegerField(
        null=True, blank=True), default=list)
    last_draft_pick = models.IntegerField(null=True, blank=True, default=None)
    last_person_picking = models.IntegerField(
        null=True, blank=True, default=None)

    @property
    def round_length(self):
        return len(self.draft_order)

    def __str__(self):
        return f"{self.name}"


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    points = models.IntegerField()
    player_id = models.CharField(max_length=50, null=True, blank=True)
    team_id = models.ForeignKey(
        'Team', on_delete=models.CASCADE, related_name='player', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.team_id.name}"


class People(models.Model):
    name = models.CharField(max_length=50)
    players = models.ManyToManyField(Player, blank=True)
    group_id = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='peoples', null=True, blank=True)

    @property
    def total_points(self):
        total_points = 0
        for player in self.players.all():
            total_points += player.points
        return total_points

    @property
    def player_count(self):
        return self.players.all().count()

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    knocked_out = models.BooleanField()
    team_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"
