from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def upload(request):
    return render(request,'file_sharing/upload.html')


def download(request):
    return render(request,'file_sharing/download.html')

def file_view(request):
    return render(request,'file_sharing/file_view.html')