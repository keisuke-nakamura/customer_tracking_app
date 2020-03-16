from django.urls import path
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('index_tour/', views.index_tour, name='index_tour'),
    path('registration/', views.registration, name='registration'),
    path('registration_tour/', views.registration_tour, name='registration_tour'),
    path('unassigned/', views.unassigned, name='unassigned'),
    path('unassigned_detail/', views.unassigned_detail, name='unassigned_detail'),
    path('unassigned_tour/', views.unassigned_tour, name='unassigned_tour'),
    path('unassigned_detail_tour/', views.unassigned_detail_tour, name='unassigned_detail_tour'),
    path('authority/', views.authority, name='authority'),
    path('authority_tour/', views.authority_tour, name='authority_tour'),
    path('account/', views.account, name='account'),
    path('account_tour/', views.account_tour, name='account_tour'),
    path('tour/', views.tour, name='tour'),
    path('customer_detail/<int:potential_customer_id>', views.customer_detail, name='customer_detail'),
    path('customer_detail_tour/', views.customer_detail_tour, name='customer_detail_tour'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (
        url(r'^your_app/', include(debug_toolbar.urls)),
    )