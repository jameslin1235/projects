from django.contrib import admin
from .models import User, UserPost, UserTag, UserUser
# Register your models here.
admin.site.register(User)
admin.site.register(UserPost)
admin.site.register(UserTag)
admin.site.register(UserUser)
