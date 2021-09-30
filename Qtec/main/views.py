from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from main.form import CreateUser
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('/')


    form = CreateUser()

    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')



    context = {
        'form':form
    }
    return render(request, 'main/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    context = {
        'message':""
    }

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username, password= password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else :
            context['message'] = "username or password is in correct sir or mam"
    return render(request,'main/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('/login')

