from django.shortcuts import render

# Create your views here.


def storePage(request):

    return render(request, 'store/storePage.html')