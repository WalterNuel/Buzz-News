from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render

import requests

from .models import *


# Create your views here.
def index(request):
  user = User.objects.get(username=request.user.username)
  profile = Profile.objects.get(username=user)
  interests = PickedInterests.objects.filter(user=profile)
  query = request.GET.get('search')

  key = "YOUR_API_KEY"
  url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_API_KEY'

  response = requests.get(url).json()
  news_articles = response

  if query:
    query = query.lower()
    url = f"https://newsapi.org/v2/everything?q={query.lower()}&apiKey=YOUR_API_KEY"
    response = requests.get(url).json()
    news_articles = response

    # Delete the saved news articles from the session
  # Check if the news articles data exists in the session
  # elif 'news_articles' in request.session:
  #     # Retrieve the news articles data from the session
  #     news_articles = request.session['news_articles']
  # else:
  #     # Make a new API request to get the news articles
  #     response = requests.get(url).json()
  #     news_articles = response
  #     # Save the API response in the session for future use
  #     request.session['news_articles'] = news_articles
  #     request.session.save()
  

    a = news_articles['articles']
    desc = []
    title = []
    img = []
    author = []

    for i in range(len(a)):
      f = a[i]
      title.append(f['title'])
      desc.append(f['description'])
      img.append(f['urlToImage'])
      author.append(f['author'])

    my_list = zip(title, desc, img, author)

  else:
    response = requests.get(url).json()
    news_articles = response
    a = news_articles['articles']
    desc = []
    title = []
    img = []
    author = []

    for i in range(len(a)):
      f = a[i]
      title.append(f['title'])
      desc.append(f['description'])
      img.append(f['urlToImage'])
      author.append(f['author'])

    my_list = zip(title, desc, img, author)
  
  context = {
    'lvl':my_list,
    'query':query
  }

  return render(request, 'index.html', context)


def landing(request):
  return render(request, 'landing.html')

def sign_up(request):
  if request.method == 'POST':
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password == password2:
      if User.objects.filter(username=username).exists():
        messages.info(request, 'Username Taken')
        return redirect('landing')
      else:
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password)
        user.save()

        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(username=user_model, first_name=first_name, last_name=last_name)
        new_profile.save()
        return redirect('index')