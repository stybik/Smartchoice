from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views
app_name = 'bestphone'

urlpatterns = [
    #path('index/', views.index),
    url(r'^home/',views.home,name = "home"),
    url(r'^index/',views.index,name = "index"),
]