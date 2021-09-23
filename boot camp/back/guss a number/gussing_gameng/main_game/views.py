from django.shortcuts import render
import random


# Create your views here.
def home(request):
    context = {
        'text': 'welcome to game',
        'guess': ' guess a number'

    }

    if request.method == 'GET':

        return render(request,'main_game/index.html',context)
    elif request.method == 'POST':
        guess = int(request.POST['num'])
        number = random.randint(1, 5)



        if guess < number:
            context['text'] = 'Your guess is too low'
        elif guess > number:
            context['text'] = 'Your guess is too high'
        elif guess == number:
            context['text'] = 'You go to next round'
        context['guess'] = 'the number is '+str(number)


        return render(request,'main_game/index.html',context)
