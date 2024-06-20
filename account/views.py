from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.forms import RegistrationForm
from account.models import Account
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def register(request):

    if request.method == "POST":
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            firstName = register_form.cleaned_data['first_name']
            lastName = register_form.cleaned_data['last_name']
            emailId = register_form.cleaned_data['email']
            phoneNumber = register_form.cleaned_data['phone_number']
            setPassword = register_form.cleaned_data['password']
            username  = emailId.split('@')[0]

            user = Account.objects.create_user(
                first_name = firstName,
                last_name = lastName,
                email = emailId,
                username = username,
                password = setPassword
            )
            user.phone_number = phoneNumber
            user.save()
            
            return redirect('signin')
    else:
        register_form = RegistrationForm()

    context={
        'form': register_form,
    }

    return render(request, 'accounts/register.html', context)


def sign_in(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user) 
            return redirect('dashboard')

    return render(request, 'accounts/signin.html')


def sign_out(request):
    return redirect('homePage')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')