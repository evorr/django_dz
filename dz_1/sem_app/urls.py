from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('start', views.head, name='head'),
 path('about', views.about_me, name='about_me'),
]
