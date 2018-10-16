from django.db import models

# Create your models here.
class Tweet(models.Model):
    Created_Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    Tweet_id = models.CharField(max_length=255)
    Tweet_Date = models.DateTimeField()
    Tweet_Text = models.CharField(max_length=255)
    objects = models.Manager()

    class Meta:
        db_table = 'Zappy_Tweet'