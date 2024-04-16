#ChatProject>ChatApp>views.py
# Create your views here.
from django.shortcuts import render, redirect
from .models import *

def CreateRoom(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        # Either get room object or create if doesn't exist
        try:
            get_room = Room.objects.get(room_name=room)
            return redirect('room', room_name=room, username=username)
        # If room does not exist we will create it and save
        except Room.DoesNotExist:
            new_room = Room(room_name = room)
            new_room.save()
            return redirect('room', room_name=room, username=username)
    rooms = Room.objects.all().values_list('room_name', flat=True)
    return render(request, 'index.html', {'rooms': rooms})

def MessageView(request, room_name, username):
    # Get room object by name
    get_room = Room.objects.get(room_name=room_name)

    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(room=get_room, sender=username, message=message)
        new_message.save()

    get_messages= Message.objects.filter(room=get_room)
    
    context = {
        "messages": get_messages,
        "user": username,
        "room_name": room_name,
    }
    return render(request, 'message.html', context)