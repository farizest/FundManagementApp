from django.shortcuts import render
from .models import Event

def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'home.html', context)

def add(request):
    return render(request, 'event-add.html')