from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from project1.project1.tags.models import Tag
from project1.project1.posts.models import Post

# Create your models here.

# def get_upload_location(instance, filename):
#     return "users/%s/%s" % (instance.user.username,filename)

class User(AbstractUser):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    tags = models.ManyToManyField(Tag)
    posts = models.ManyToManyField(Post)
    users = models.ManyToManyField("self", symmetrical=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )
    industry = models.CharField(
        max_length=100,
        blank=True
    )
    position = models.CharField(
        max_length=100,
        blank=True
    )
    company = models.CharField(
        max_length=100,
        blank=True
    )
    school = models.CharField(
        max_length=100,
        blank=True
    )
    concentration = models.CharField(
        max_length=100,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    credential = models.CharField(
        max_length=100,
        blank=True
    )
    description = models.TextField(
        blank=True,
    )
    # avatar_width_field = models.IntegerField()
    # avatar_height_field = models.IntegerField()
    # avatar = models.ImageField(
    #     upload_to = get_upload_location,
    #     height_field = "avatar_height_field",
    #     width_field = "avatar_width_field",
    #     blank=True,
    #     default= "default/avatar.jpg"
    # )

    def __str__(self):
        return '%s' % (self.username)

    def get_absolute_url(self):
        return reverse('users:user_detail', kwargs={'pk': self.pk})



# print(type(User._meta.get_field('posts')))
# print(User._meta.get_field('posts').related_name)
# print(User._meta.get_field('posts').description)
