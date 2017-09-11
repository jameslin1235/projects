from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tag_list, name='tag_list'),
    url(r'^(?P<pk>\d+)/$', views.tag_detail, name='tag_detail'),
]