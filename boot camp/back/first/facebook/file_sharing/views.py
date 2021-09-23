from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

context = {
    'upload':0,
    'download':0,
    'file_view':0,
}

def upload(request):
    context['upload'] += 1
    return render(request,'file_sharing/upload.html',context)


def download(request):
    context['download'] += 1
    return render(request,'file_sharing/download.html',context)

def file_view(request):
    context['file_view'] += 1
    return render(request,'file_sharing/file_view.html',context)