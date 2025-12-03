from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, "Perfil/home.html")
