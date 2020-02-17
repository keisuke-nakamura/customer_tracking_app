from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def login(request):

    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

