from django.contrib import admin
from .models import Post
from .models import Tweet

admin.site.register(Post)
admin.site.register(Tweet)