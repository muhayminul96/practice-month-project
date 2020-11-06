from django.shortcuts import render
from django.http import HttpResponse
import re


def cal(reguest):
    if reguest.method=="GET":
        return render(reguest, 'calculator/from.html')
    elif reguest.method=="POST":
        passw = reguest.POST['pass']
        context = {
            'output' : 'none'
        }

        if len(passw)>7:
            if len(re.findall(r'[A-Z]', passw))>0:
                if len(re.findall(r'[a-z]', passw))>0:
                    if len(re.findall(r'[\!\"\#\$\%\&\'\(\)\*\+\,\-\.\/:\;\<\=\>\?\@\\[\\\]\^\_\\`\{\|\}\~]', passw)) > 0:
                        if re.match(r'[\d]', passw):
                            context['output'] = "First digit can't be number"
                        else:
                            context['output'] = 'PASS ALL CASE'
                    else:
                        context['output'] = "error password need at least one special characters "

                else:
                    context['output'] = "error password need at least one Lowercase"
            else:
                context['output'] = "error password need at least one Uppercase"

        else:
            context['output'] = "password is sort , password have at least 8 character"



        return render(reguest, 'calculator/output.html', context)


def home(request):
    return HttpResponse("<h1>welcome</h1>")
