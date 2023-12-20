from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .import views

urlpatterns = [
    path('<int:id>/produit', views.produit,name="produit"),
    path('<int:id>/liste_produits',views.liste_produits,name="liste_produits"),   
    #path('newest',views.liste_produits,name="liste_produits"),   
    path('invoice/', views.invoice, name='invoice'),
    path('create_order/', views.create_order, name='create_order'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

