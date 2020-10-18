from django.shortcuts import render

def home(request,num1,num2):
    sum =num1 + num2
    context={
        'name': "rohimuddin",
        'food': 'rice',
        'age': '23',
        'sum': sum
    }
    return render(request,'secondary/home.html',context)
