from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tweet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    reply_count = models.IntegerField(default=0)
    retweet_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)

    def publish(self):
        self.save()

    def __str__(self):
        return str(self.id)