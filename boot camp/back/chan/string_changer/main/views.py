from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'tex':''
    }
    if request.method == 'GET':

        return render(request,'main/home.html',context)
    elif request.method == 'POST':
        org = request.POST['main']
        rep = request.POST['temp']
        le = request.FILES['txfile']
        tfile = le.read().decode('utf8')
        print(tfile)
        txt = tfile.replace(org,rep)

        context['tex'] = txt


        return render(request,'main/home.html',context)

