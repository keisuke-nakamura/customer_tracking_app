from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        return render(request, 'main.html')

    return render(request, 'main.html')
    # return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')

