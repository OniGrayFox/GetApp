from django.contrib import admin
from django.urls import path,include
from .views import get_app
urlpatterns = [

    path('', get_app),

]
