from django.shortcuts import render
from main.models import *

# Create your views here.

def home(request):

    ar = {}
    main_arr = []


    word = Word.objects.all()
    context = {

        'word' : word,


    }
    if request.method == "GET":
        return render(request,'main/index.html',context)
    elif request.method == "POST":
        cl = Word.objects.all()
        cl.delete()

        txt = request.POST['txt2']
        arr = txt.split()
        for i in arr:
            if i in main_arr:
                ar[i] = ar[i]+1
            else:
                main_arr.append(i)
                ar[i] = 1
        for key,value in ar.items():
            Word.objects.create(word=key,num=value)
        return render(request, 'main/index.html', context)






        return render(request,'main/index.html',context)

