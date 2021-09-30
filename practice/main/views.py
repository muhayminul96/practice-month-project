from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json
import urllib.request


# Create your views here.


def home(request):
    persons = Person.objects.all()
    context = {
        "persons": persons,
        'names': ['korim', 'rohiom', "kuddus",'445',666 ]

    }
    return render(request, 'home.html', context)


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
                return redirect('/register')

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

def log_out(request):
    auth.logout(request)
    return redirect('/login')


def name(request,name):
    context = {
        'name': name
    }
    return render(request, 'ditails.html', context)

def weather(request):

    city = False
    context = {
        "city": city,

    }
    if request.method == "POST":
        city = request.POST['city']
        context['city'] = city
        try:
            res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e194ffdc3e0a7da134c5aa9635213b3d')
            json_data = json.load(res)
            context['data'] = json_data
        except:
            return render(request, 'weather.html', context)


    return render(request, 'weather.html', context)

