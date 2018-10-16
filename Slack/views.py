import os

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
import time
from slackclient import SlackClient

# Create your views here.

def Slack(self):

    token = 'xoxb-455726381732-456117813509-o1J3EH1VMs1eLuUAO6rT45cg'
    sc = SlackClient(token)

    if sc.rtm_connect():
        while True:
            event = sc.rtm_read()
            if "go" in event.text:
                print("call get_tweets")
            time.sleep(1)
    else:
        print('Connection Failed, invalid token?')

    return Response(status=status.HTTP_200_OK)
