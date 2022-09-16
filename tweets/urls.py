from django.urls import path

from tweets.views import (home_view,
                          room1_view,
                          tweet_action_view,
                          tweet_datail_view,
                          tweet_list_view,
                          tweet_create_view,
                          tweet_delete_view )
'''
CLIENT
Base ENDPOINT /api/tweets/
'''

urlpatterns = [
    path('', tweet_list_view),
    path('action/', tweet_action_view),
    path('create/', tweet_create_view),
    path('<int:tweet_id>/', tweet_datail_view),
    path('<int:tweet_id>/delete/', tweet_delete_view),
]
 