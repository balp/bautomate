from django.db import models

# Create your models here.

class TelldusDevice(models.Model):
    # Dev: 1: Advent_Datorrum = arctech, selflearning-switch, 1
    # bool on, just a guess.
    td_id = models.IntegerField()
    name = models.CharField(max_length=200)
    on = models.BooleanField()
    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(TelldusDevice)
    def __unicode__(self):
        return self.name
