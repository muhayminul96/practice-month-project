from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

context = {
    'blocking':0,
    'follow':0,
    'friend_request':0,
}

def blocking(request):
    context['blocking'] +=1
    return render(request,'prosseing/blocking.html',context)


def follow(request):
    context['follow'] +=1

    return render(request,'prosseing/follow.html',context)


def friend_request(request):
    context['friend_request'] +=1

    return render(request, 'prosseing/freind_request.html',context)
