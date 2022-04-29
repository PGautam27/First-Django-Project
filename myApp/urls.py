from django.contrib import admin
from django.urls import path, include
from myApp import views

urlpatterns = [
    path("",views.index, name='myApp')
]