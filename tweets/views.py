from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
  return render(request, "pages/home.html", context={}, status=200) 

def room1_view(request, *args, **kwargs):
  return HttpResponse("<h1>This is sean's private room!</h1>")

def tweet_datail_view(request, tweet_id, *args, **kwargs):
  """
  REST API VIEW
  Consume by JavaScript or Swift/Java/iOS/Android
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