from django.shortcuts import render, HttpResponse, redirect
import random
from time import strftime
from datetime import datetime

def index(request):
  # response = "hello world"
  print '*' * 80
  print 'hello'
  return render(request, 'first_app/index.html')

def process(request):
  print '*' * 80
  location = request.POST['location']
  print request.POST['location']
  location_map = {
    'cave': random.randint(3,7),
    'house': random.randint(2,5),
    'farm': random.randint(7,15),
    'casino': random.randint(-50,50)
  }

  if location in location_map:
    curr_gold = location_map[location]
    date_time = datetime.now().strftime("%H:%m:%p on %d/%m/%y")

    if not 'curr_gold' in request.session:
      request.session['curr_gold'] = 0
    else:
      request.session['curr_gold'] += curr_gold

    if curr_gold >= 0:
      css_class = "green"
      action_string = "Won "
    else:
      css_class = "red"
      action_string = "Lost "

    action_string += " {} from {} at {}".format(str(curr_gold), location, date_time)

    action = {
      'class': css_class,
      'description': action_string
    }

    if not 'history' in request.session:
      request.session['history'] = []
    else:
      request.session['history'].append(action)

    print request.session['curr_gold']

  return redirect('/')

def reset(request):
  request.session.clear()
  return redirect('/')
