from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return render(request,'messenger/about.html')
def home(request):
    return render(request, 'messenger/home.html')
def contact(request):
    return render(request, 'messenger/contract.html')
