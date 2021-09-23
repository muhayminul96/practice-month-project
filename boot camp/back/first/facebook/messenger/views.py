from django.shortcuts import render
from django.http import HttpResponse

context = {
    'home': 0,
    'about': 0,
    'contract': 0,
}

def about(request):
    context['about'] += 1
    return render(request,'messenger/about.html',context)
def home(request):
    context['home'] += 1
    return render(request, 'messenger/home.html',context)
def contact(request):
    context['contract'] += 1
    return render(request, 'messenger/contract.html',context)
