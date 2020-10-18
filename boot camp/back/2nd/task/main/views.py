from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'name': "muhayminul",
        'email': 'muhayminul@mail.com',
        'age' : '24'
    }
    return render(request,'main/home.html',context)