from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from Planeum.settings import MEDIA_URL
from chat.models import Room, Message
from django.views.decorators.csrf import csrf_protect
# Create your views here.
def chathome(request):
    return render(request, 'chathome.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username':username,
        'room':room,
        'room_details':room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/chat/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/chat/'+room+'/?username='+username)

@csrf_protect
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    f = request.FILES.get('mfile')
    new_message = Message.objects.create(value=message, user=username, room=room_id, file=f)
    new_message.save()
    return HttpResponse("Message send successfuly")
    
def get_messages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})