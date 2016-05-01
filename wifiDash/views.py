from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import wifiMeasurement

# Create your views here.
def measurementList(request):
    measurements = wifiMeasurement.objects.all().order_by('dateTime')
    paginator = Paginator(measurements, 200)
    page = request.GET.get('page')
    try:
        measurementPage = paginator.page(page)
    except PageNotAnInteger:
        measurementPage = paginator.page(1)
    except EmptyPage:
        measurementPage = paginator.page(paginator.num_pages)
        
    return render(request, 'wifiDash/home.html',
                  {'measurements': measurementPage})

def measurement(request, pk):
    measurement = get_object_or_404(wifiMeasurement, pk=pk)
    return render(request, 'wifiDash/one.html',
                  {'measurement': measurement})
