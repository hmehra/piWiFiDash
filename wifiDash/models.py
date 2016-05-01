from django.db import models
from django.utils import timezone

# Create your models here.
class wifiMeasurement(models.Model):
    id       = models.IntegerField(primary_key=True)
    dateTime = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length = 200)
    server   = models.CharField(max_length = 200)
    download = models.FloatField()
    upload   = models.FloatField()
    ping     = models.FloatField()
    distance = models.FloatField()
