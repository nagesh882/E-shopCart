from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def register(request):
    return render(request, 'accounts/register.html')


def sign_in(request):
    return render(request, 'accounts/signin.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')