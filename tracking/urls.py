from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('registration_tour/', views.registration_tour, name='registration_tour'),
    path('unassigned/', views.unassigned, name='unassigned'),
    path('authority/', views.authority, name='authority'),
    path('authority_tour/', views.authority_tour, name='authority_tour'),
    path('tour/', views.tour, name='tour'),
]
