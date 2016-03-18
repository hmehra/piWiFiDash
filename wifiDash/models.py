from django.db import models
from django.utils import timezone

# Create your models here.
class wifiMeasurement(models.Model):
    dateTime = models.DateTimeField(default=timezone.now)
    server = models.CharField(max_length = 200)
    download = models.FloatField()
    upload = models.FloatField()
    ping = models.FloatField()
