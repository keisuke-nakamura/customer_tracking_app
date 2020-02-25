from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, 'customer_registration.html')


def registration_tour(request):
    return render(request, 'customer_registration_tour.html')


def unassigned(request):
    return render(request, 'unassigned.html')


def authority(request):
    return render(request, 'authority.html')


def authority_tour(request):
    return render(request, 'authority_tour.html')


def tour(request):
    return render(request, 'tour.html')


def customer_detail(request):
    return render(request, 'customer_detail.html')

