from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def blocking(request):
    return render(request,'prosseing/blocking.html')


def follow(request):
    return render(request,'prosseing/follow.html')


def friend_request(request):
    return render(request, 'prosseing/freind_request.html')