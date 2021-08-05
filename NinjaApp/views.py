from django.shortcuts import render, redirect
import random
import datetime
import time
import sys

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'message' not in request. session:
        request.session['message'] = []

    return render(request, 'index.html')


def process(request, source):
    now = datetime.datetime.now().strftime("%A, %B %d, %Y - %I:%M %p")
    if source == 'farm':
        rand = random.randint(10,21)
        request.session['gold'] += rand
        request.session['message'].append("Earned {} gold from the farm! ({})".format(rand, now))
    elif source == "cave":
        rand = random.randrange(5,11)
        request.session['gold'] += rand
        request.session['message'].append("Earned {} gold from the cave!  ({})".format(rand, now))
    elif source == "house":
        rand = random.randrange(2,6)
        request.session['gold'] += rand
        request.session['message'].append("Earned {} gold from the house!  ({})".format(rand, now))
    elif source == "casino":
        chance = random.randint(0,2)
        if chance == 1:
            rand = random.randint(0,51)
            request.session['gold'] += rand
            request.session['message'].append("Earned {} gold from the casino!  ({})".format(rand, now))
        else:
            rand = random.randint(0,51)
            request.session['gold'] -= rand
            request.session['message'].append("Lost {} gold from the casino! ({})".format(rand, now))

    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['message'] = []

    return redirect('/')