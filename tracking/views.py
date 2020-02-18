from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def login(request):
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, 'customer_registration.html')


def unassigned(request):
    return render(request, 'unassigned.html')


def how_to_use(request):
    return render(request, 'how_to_use.html')


def tour(request):
    return render(request, 'tour.html')


