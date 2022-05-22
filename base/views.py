from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'lets learn django'},
#     {'id': 2, 'name': 'lets learn django templates'},
#     {'id': 3, 'name': 'django frontend'}
# ]
def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms':rooms})

def room(request, pk):
    room = Room.objects.get(id=pk)
    context={'room':room}
    return render(request, 'base/room.html',context)