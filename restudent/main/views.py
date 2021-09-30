from django.shortcuts import render,redirect
from main.models import *
# Create your views here.


def home(request):
    context={

    }
    events = Event.objects.all()
    items = Items.objects.all()

    context['events'] = events
    context['items'] = items


    return render(request,'main/index.html', context)


def tableForm(request):

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']

        Table.objects.create(name=name,email=email,phone=phone,date=date,time=time,numberOfPeople=people,message=message)



    return redirect('/')

def contractForm(request):

    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contract.objects.create(name=name, email=email, subject=subject, message=message)



    return redirect('/')


