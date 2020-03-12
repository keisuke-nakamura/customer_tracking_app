from django.shortcuts import render, redirect
from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import Http404
from django.urls import reverse

from .models import PotentialCustomers, TPremise, Media


def login(request):
    return render(request, 'login.html')


def index(request):
    potential_customers = PotentialCustomers.objects.select_related('int_media').select_related('int_information_premise').order_by('id')

    context = {'potential_customers': potential_customers}
    return render(request, 'index.html', context)


def index_tour(request):
    return render(request, 'index_tour.html')


def registration(request):
    return render(request, 'customer_registration.html')


def registration_tour(request):
    return render(request, 'customer_registration_tour.html')


def unassigned(request):
    return render(request, 'unassigned.html')


def unassigned_detail(request):
    return render(request, 'unassigned_detail.html')


def unassigned_tour(request):
    return render(request, 'unassigned_tour.html')


def unassigned_detail_tour(request):
    return render(request, 'unassigned_detail_tour.html')


def authority(request):
    return render(request, 'authority.html')


def authority_tour(request):
    return render(request, 'authority_tour.html')


def account(request):
    return render(request, 'account.html')


def account_tour(request):
    return render(request, 'account_tour.html')


def tour(request):
    return render(request, 'tour.html')


def customer_detail(request, potential_customer_id):

    try:
        potential_customer = PotentialCustomers.objects.get(pk=potential_customer_id)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")

    potential_customer = {'potential_customer': potential_customer}
    return render(request, 'customer_detail.html', potential_customer)


def customer_detail_tour(request):
    return render(request, 'customer_detail_tour.html')


