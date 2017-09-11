from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.title)

    def get_absolute_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.pk})

    # def get_edit_url(self):
    #     return reverse("posts:post_edit", kwargs={"pk": self.pk})
