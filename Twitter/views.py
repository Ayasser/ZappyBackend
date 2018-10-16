from django.shortcuts import render

# Create your views here.
import tweepy
from rest_framework import status, viewsets, filters, pagination, generics
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Tweet
from .serializers import TweetSerializer
from django.conf import settings

class get_Tweets(generics.RetrieveAPIView):
    """
    get_Tweets is view that call when slack message contain 'go'
    it's retrieve all tweets and only save new tweets
    """

    def retrieve(self, request):

        consumer_key = getattr(settings, 'CONSUMER_KEY')
        consumer_secret = getattr(settings, 'CONSUMER_SECRET')
        access_token = getattr(settings, 'ACCESS_TOKEN')
        access_token_secret = getattr(settings, 'ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        new_tweets = api.user_timeline(screen_name = 'FictionFone',count=200)

        for tweet in new_tweets:
            old_tweet = Tweet.objects.filter(Tweet_id=tweet.id).first()
            tweet_obj = Tweet()

            if old_tweet is None:
                tweet_obj.Tweet_id = tweet.id
                tweet_obj.Tweet_Date = tweet.created_at
                tweet_obj.Tweet_Text = tweet.text
                tweet_obj.save()
        return Response(status=status.HTTP_200_OK)



class TweetViewSet(ListAPIView):
    """
    list View Set for Tweets
    """
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

