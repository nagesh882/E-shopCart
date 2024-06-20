from django.shortcuts import render
from django.http import HttpResponse
from account.forms import RegistrationForm

# Create your views here.


def register(request):

    if request.method == "POST":
        register_form = RegistrationForm()
    else:
        register_form = RegistrationForm()

    context={
        'form': register_form,
    }

    return render(request, 'accounts/register.html', context)


def sign_in(request):
    return render(request, 'accounts/signin.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')