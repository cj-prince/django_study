from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
rooms = [
    {'id': 1, 'name': 'lets learn django'},
    {'id': 2, 'name': 'lets learn django templates'},
    {'id': 3, 'name': 'django frontend'}
]
def home(request):
    return render(request, 'home.html', {'rooms':rooms})

def room(request):
    return render(request, 'room.html')