from django.shortcuts import render


def draws_home(request):
    return render(request, "draws/home.html")