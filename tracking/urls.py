from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('index_tour/', views.index_tour, name='index_tour'),
    path('registration/', views.registration, name='registration'),
    path('registration_tour/', views.registration_tour, name='registration_tour'),
    path('unassigned/', views.unassigned, name='unassigned'),
    path('unassigned_detail/', views.unassigned_detail, name='unassigned_detail'),
    path('authority/', views.authority, name='authority'),
    path('authority_tour/', views.authority_tour, name='authority_tour'),
    path('tour/', views.tour, name='tour'),
    path('customer_detail/', views.customer_detail, name='customer_detail'),
    path('customer_detail_tour/', views.customer_detail_tour, name='customer_detail_tour'),
]
