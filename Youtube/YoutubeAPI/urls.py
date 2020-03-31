from django.conf.urls import url,include
from django.contrib import admin

from django.urls import path
from . import views

urlpatterns = [

    url('admin/', admin.site.urls), #this is simple admin url path
    path('',views.Song.as_view())   #this is path that get data from views and other is model class
]
