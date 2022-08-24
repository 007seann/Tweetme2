from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
  return HttpResponse("<h1>HELLO World!</h1>")

def room1_view(request, *args, **kwargs):
  return HttpResponse("<h1>This is sean's private room!</h1>")

def tweet_datail_view(request, tweet_id, *args, **kwargs):
  try:
    obj = Tweet.objects.get(id=tweet_id)
  except:
    raise Http404
  return HttpResponse(f"<h1>HELLO {tweet_id} --- {obj.content}!</h1>")