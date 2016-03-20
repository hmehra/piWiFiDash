from django.shortcuts import render

# Create your views here.
def measurementList(request):
    return render(request, 'wifiDash/home.html', {})
