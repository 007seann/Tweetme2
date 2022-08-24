from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
  print(args, kwargs)
  return HttpResponse("<h1>HELLO World!</h1>")

def room1_view(request, *args, **kwargs):
  return HttpResponse("<h1>This is sean's private room!</h1>")

def tweet_datail_view(request, tweet_id, *args, **kwargs):
  return HttpResponse(f"<h1>HELLO {tweet_id}!</h1>")