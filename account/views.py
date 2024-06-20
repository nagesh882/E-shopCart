from django.shortcuts import render

# Create your views here.


def sign_up(request):
    return render(request, 'accounts/signup.html')



def dashboard(request):
    return render(request, 'accounts/dashboard.html')