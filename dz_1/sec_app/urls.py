from django.urls import path
from . import views


urlpatterns = [
 path('coin/', views.coin, name='coin'),
 path('cube/', views.cube, name='cube'),
 path('random/', views.rnd100, name='rnd100')
]
