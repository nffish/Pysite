from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=300, default='Title')
    # author = models.ForeignKey(User, related_name="blog_posts")
    content = models.TextField(null=True)
    # publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
