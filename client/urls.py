from django.contrib import admin
from django.urls import path,include

from .import views

urlpatterns = [   
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('espace_utilisateur/', views.espace_utilisateur, name='espace_utilisateur'),    
    path('search/', views.search_feature, name='search-view'),
     path('signup/', views.signup, name='signup'),
    path('categories/', views.categories, name='categories'),
    path('deleteorder/', views.deleteorder, name='deleteorder'),
]    