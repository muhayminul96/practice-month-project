from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    if request.method == "POST":
        room_name = request.POST['room']
        username = request.POST['name']

        if Room.objects.filter(room_name=room_name).exists():
            return redirect('room/' +str(room_name))
        else:
            room = Room.objects.create(room_name=room_name)
            room.save()
            return redirect('/room/' + room_name)

    else:
        return render(request,'home.html')

@login_required
def chat(request,room):
    context = {

    }

    if request.method=='POST':
        text = request.POST['text']
        r = Room.objects.get(room_name=room)

        txt = Text.objects.create(username=request.user.username, text=text, room=r)
        txt.save()

    texts = Text.objects.filter(room__room_name=room)
    context['texts'] = texts

    return render(request,'chating.html',context)



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password1 == password:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username exist')
                return redirect('/register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is exists ')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'successfully registerer ')
                return redirect('/login')

        else:
            messages.info(request, 'password not same')
            return redirect('/register')
    else:

        return render(request, 'regi.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'password or username error')
            return redirect('/login')


    else:

        return render(request, 'signin.html')

@login_required
def log_out(request):
    auth.logout(request)
    return redirect('login')

