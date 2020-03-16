from django.shortcuts import render, redirect
from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.http import Http404
from django.urls import reverse
from django.db.models import Prefetch
import itertools

from .models import PotentialCustomers, TPremise, Media, TNameList, TUser, TDealer, Authority, UlAuthority


# ログイン
def login(request):
    return render(request, 'login.html')


# 見込客一覧
def index(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=True).select_related('int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404('customer does not exists')
    context = {'potential_customers': potential_customers}
    return render(request, 'index.html', context)


def index_tour(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=True).select_related(
            'int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404('customer does not exists')
    context = {'potential_customers': potential_customers}
    return render(request, 'index_tour.html', context)


def customer_detail(request, potential_customer_id):
    try:
        potential_customer = PotentialCustomers.objects.select_related('int_information_premise').get(pk=potential_customer_id)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")
    context = {'potential_customer': potential_customer}
    return render(request, 'customer_detail.html', context)


def customer_detail_tour(request):
    return render(request, 'customer_detail_tour.html')


def registration(request):
    return render(request, 'customer_registration.html')


def registration_tour(request):
    return render(request, 'customer_registration_tour.html')


def unassigned(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=False).select_related('int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exists")
    context = {'potential_customers': potential_customers}
    return render(request, 'unassigned.html', context)


def unassigned_detail(request, potential_customer_id):
    try:
        potential_customer = PotentialCustomers.objects.select_related('int_information_premise').get(pk=potential_customer_id)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")
    context = {'potential_customer': potential_customer}
    return render(request, 'unassigned_detail.html', context)


def unassigned_tour(request):
    try:
        potential_customers = PotentialCustomers.objects.filter(bol_assigned=False).select_related('int_media').select_related('int_information_premise').order_by('id')
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exists")
    context = {'potential_customers': potential_customers}
    return render(request, 'unassigned_tour.html', context)


def unassigned_detail_tour(request, potential_customer_id):
    try:
        potential_customer = PotentialCustomers.objects.select_related('int_information_premise').get(pk=potential_customer_id)
    except PotentialCustomers.DoesNotExist:
        raise Http404("customer does not exist")
    context = {'potential_customer': potential_customer}
    return render(request, 'unassigned_detail_tour.html', context)


def authority(request):
    return render(request, 'authority.html')


def authority_tour(request):
    return render(request, 'authority_tour.html')


def account(request):
    try:
        users = Authority.objects.select_related('int_user', 'int_auth', 'int_user__int_dealer__int_name').order_by('int_user')

    except TUser.DoesNotExist:
        raise Http404("user does not exists")
    context = {'users': users}
    return render(request, 'account.html', context)


def account_tour(request):
    return render(request, 'account_tour.html')


def tour(request):
    return render(request, 'tour.html')





