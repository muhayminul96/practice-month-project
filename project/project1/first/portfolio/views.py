from django.shortcuts import render

def index(request):
    return render(request,'portfolio/index.html')
def index1(request):
    return render(request,'portfolio/index1.html')

