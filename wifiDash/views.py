from django.shortcuts import render
from .models import wifiMeasurement

# Create your views here.
def measurementList(request):
    measurements = wifiMeasurement.objects.all().order_by('dateTime')
    return render(request, 'wifiDash/home.html',
                  {'measurements': measurements})
