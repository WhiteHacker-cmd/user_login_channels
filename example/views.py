from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import RoomForm
from .models import Room, Message

# Create your views here.

User = get_user_model()


def user_list1(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
    
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'example/user_list1.html', {'users': users})


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'example/create_room.html', context)

@login_required(login_url='/log_in/')
def user_list(request):
    users = User.objects.select_related('logged_in_user')
    for user in users:
    
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'example/user_list.html', {'users': users})



def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('example:user_list'))
        else:
            print(form.errors)
    return render(request, 'example/log_in.html', {'form': form})



def log_out(request):
    logout(request)
    return redirect(reverse('example:log_in'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('example:log_in'))
        else:
            print(form.errors)
    return render(request, 'example/sign_up.html', {'form': form})


@login_required(login_url='/log_in/')
def chat_view(request, pk):
    room = Room.objects.get(label=pk)
    messages = Message.objects.filter(room=room)
    context = {'messages': messages}
    return render(request, 'example/chat_room.html', context)