from django.contrib import admin
from django.urls import path, re_path
from posts import views
import re

urlpatterns = [
   	path('', views.post_home, name='home'),
   	path('list', views.post_list, name='list'),
   	path('create', views.post_create, name='create'),
   	re_path(r'^(?P<id>\d+)/$', views.post_detail, name='detail'),
   	re_path(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
   	re_path(r'^(?P<id>\d+)/delete/$', views.post_delete, name='delete')
]