from django.urls import path
from . import views

urlpatterns = [
  
    path('vieworder/', views.vieworder, name='vieworder'),
]