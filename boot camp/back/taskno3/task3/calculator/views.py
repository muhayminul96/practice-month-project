from django.shortcuts import render
from django.http import HttpResponse


def cal(reguest):
    if reguest.method=="GET":
        return render(reguest, 'calculator/from.html')
    elif reguest.method=="POST":
        num1 = int(reguest.POST['num1'])
        num2 = int(reguest.POST['num2'])
        opp = reguest.POST['opp']

        if opp=='+':
            context = {
                'output': num1+num2

            }
        elif opp == '-':
            context = {
                'output': num1 - num2

            }
        if opp == '*':
            context = {
                'output': num1 * num2

            }
        if opp == '/':
            context = {
                'output': num1 / num2

            }

        return render(reguest, 'calculator/output.html',context)

def home(request):
    return HttpResponse("<h1>welcome</h1>")
