from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.liste_commande),
    path('ajout_commande/', views.ajoutercommande, name='ajout_commande'),
    path('modifiercommande/<str:pk>', views.modifiercommande, name='modifiercommande'),
    path('supprimercommande/<str:pk>', views.supprimercommande, name='supprimercommande'),
]