from django.db import models
import datetime

# Create your models here.

class TelldusDevice(models.Model):
    # Dev: 1: Advent_Datorrum = arctech, selflearning-switch, 1
    # bool on, just a guess.
    td_id = models.IntegerField()
    name = models.CharField(max_length=200)
    on = models.BooleanField()
    def __unicode__(self):
        return self.name

class TimerPeriod(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def status(self, time=None):
        """True if time, defauls to now(), is in the inclusive range."""
        if None == time:
            time = datetime.now().time
        if self.start_time < self.end_time:
            return self.start_time <= time and time <= self.end_time


class Group(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(TelldusDevice)
    def __unicode__(self):
        return self.name
