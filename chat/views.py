from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import MessageForm, RoomForm
from .models import Message, Room
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    messages = Message.objects.all()
    rooms = Room.objects.filter(members__username=request.user)

    User = get_user_model()
    users = User.objects.all()
        
    context = {'messages':messages,
               'users':users,
               'rooms':rooms}
    return render(request, 'chat/home.html', context)

def delete(request, pk):
    message = Message.objects.get(id=pk)

    if request.method == "POST":
        message.delete()
        return redirect('chat:home')

    context = {}
    return render(request, 'chat/delete.html', context)

def edit(request, pk):
    message = Message.objects.get(id=pk)
    form = MessageForm(instance=message)

    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            message.save()
            return redirect('chat:home')

    context = {'form':form}
    return render(request, 'chat/edit.html', context)

def new_room(request, username):
    user = User.objects.get(username=username)
    form = RoomForm()
    room = Room()

    if request.method == "POST":
        form = RoomForm(request.POST)
        print(form)
        if form.is_valid():
            room = form.save(commit=False)
            room.save()
            for member in form.cleaned_data['members']:
                room.members.add(member)
            room.members.add(request.user)
            return redirect('chat:home')
    
    context = {'user':user,
               'form':form,}
    return render(request, 'chat/new_room.html', context)

def private_chat(request, name):
    room = Room.objects.get(name=name)
    message = Message.objects.filter(room=room)

    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid() and request.POST.get('description'):
            message = form.save(commit=False)
            message.author = request.user
            message.room = room
            message.save()
            return redirect('chat:private_chat', name=room.name)
    
    
    rooms = Room.objects.filter(members__username=request.user)
    messages = Message.objects.filter(room=room)
    context = {'messages':messages,
               'form':form,
               'rooms':rooms}
    print(message)
    return render(request, 'chat/private_chat.html', context)