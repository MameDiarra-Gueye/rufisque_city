from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('decouvrir/', views.decouvrir, name='decouvrir'),
    path('histoire/', views.histoire, name='histoire'),
    path('marches/', views.marches, name='marches'),
    path('plages/', views.plages, name='plages'),
    path('contact/', views.contact, name='contact'),
]