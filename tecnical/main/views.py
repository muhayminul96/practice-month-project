from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'main/base_layout.html')


def helloworld(request):
    return render(request,'main/helloworld.html')


