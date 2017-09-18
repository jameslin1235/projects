from django.conf import settings
from django.db import models
from django.urls import reverse
from project1.project1.posts.models import Post

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name="replies")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.content)
