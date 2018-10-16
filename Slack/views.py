import os

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status, generics
import time
from slackclient import SlackClient
from Twitter.views import TweetViewSet ,get_Tweets
from django.conf import settings


# Create your views here.
class Slack(generics.RetrieveAPIView):
    """
    Slack is view that call when to listen to channel and check messages
    """

    def retrieve(self, request):

        token = getattr(settings, 'SLACK_TOKEN')
        sc = SlackClient(token)

        if sc.rtm_connect():
            while True:
                event = sc.rtm_read()
                if "go" in event.text:
                    get_Tweets.retrieve()
                time.sleep(1)
        else:
            print('Connection Failed, invalid token?')

        return Response(status=status.HTTP_200_OK)
