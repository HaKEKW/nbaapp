from django.shortcuts import render

from nba_chat.models import Room, Message




def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'nba_chat/rooms.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(pk=pk)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'nba_chat/room.html', {'room': room, 'messages': messages})

