from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('donate/', views.donate),
]
