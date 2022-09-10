import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from tweetme2.settings import ALLOWED_HOSTS

from .forms import TweetForm
from .models import Tweet

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home_view(request, *args, **kwargs):
  return render(request, "pages/home.html", context={}, status=200) 

def tweet_create_view(request, *args, **kwargs):
  form = TweetForm(request.POST or None)
  next_url = request.POST.get("next") or None
  if form.is_valid():
    obj = form.save(commit=False)
    # do other form related logic
    obj.save()
    if request.is_ajax():
      return JsonResponse({}, status=201)
    
    if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
      return redirect(next_url)
    form = TweetForm()
  return render(request, "components/form.html", context={"form": form})


def room1_view(request, *args, **kwargs):
  return HttpResponse("<h1>This is sean's private room!</h1>")

def tweet_list_view(request, *args, **kwargs):
  """
  REST API VIEW
  Consumed by JavaScript or Swift/Java/iOS/Android
  return json data
  """
  qs = Tweet.objects.all()
  tweets_list = [{'id': x.id, 'content': x.content, "likes": random.randint(0, 144)} for x in qs]
  data = {
    'isUser': False,
    'response': tweets_list
  } 
  return JsonResponse(data) 


def tweet_datail_view(request, tweet_id, *args, **kwargs):
  """
  REST API VIEW
  Consumed by JavaScript or Swift/Java/iOS/Android
  return json data
  """
  data = {
    "id": tweet_id,
  }
  status = 200
  try:
    obj = Tweet.objects.get(id=tweet_id)
    data['content'] = obj.content
    
  except:
    data['messages'] = "Not Found"
    status = 404

  
  return JsonResponse(data, status=status) # json.dumps content_type='application/json'