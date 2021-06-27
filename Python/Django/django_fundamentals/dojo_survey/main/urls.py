from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_dash', views.createInfo),
    path('result', views.display)
]