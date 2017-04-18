from django.db import models


class Location(models.Model):

    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.IntegerField()
    dateTime = models.DateTimeField()

    class Meta:
        ordering = ('dateTime',)