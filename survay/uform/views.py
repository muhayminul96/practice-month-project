from django.shortcuts import render,redirect
from uform.models import *

# Create your views here.

def home(request):
    students = Student.objects.all()
    context = {
        'students' : students,
    }
    return render(request,'ufrom/home.html',context)

def forming(request):
    if request.method=="GET":
        return render(request,'ufrom/input.html')
    elif request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        dept = request.POST['deparment']
        gender = request.POST['gender']
        Student.objects.create(name=name,email=email,phone=phone,department=dept,gender=gender)
        print("hello boss")
        print(name,email,phone,address,gender,dept)

        return redirect('/input')

