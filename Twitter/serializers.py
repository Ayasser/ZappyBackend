from rest_framework import serializers
from .models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'id',
            'Created_Date',
            'Tweet_id',
            'Tweet_Date',
            'Tweet_Text',
        ]
        read_only_fields = ['id']
