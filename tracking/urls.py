from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('unassigned/', views.unassigned, name='unassigned'),
    path('how_to_use/', views.how_to_use, name='how_to_use'),
    path('tour/', views.tour, name='tour'),
]
