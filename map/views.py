from django.shortcuts import render
from .forms import LocationForm
from django.http import HttpResponse

def get_maps(request):
    form = LocationForm()
    if request.method == 'POST':
        print(request.POST['location'])
    return render(request, 'maps.html', {'form':form})
