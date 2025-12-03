from django.shortcuts import render , redirect
from semanas.forms import MetaForm
from semanas.models import Meta_model
# Create your views here.

def home_semanas(request):

    todas_metas = Meta_model.objects.all()

    metas = {
        'metas': todas_metas
    }

    return render(request, "Semanas/home_semanas.html",metas)

def create_meta(request):

    if request.method == "POST":
        form = MetaForm(request.POST)

        form.save()

        

        return redirect("metas")

    else:

     form = MetaForm()

     return render (request ,'Semanas/form_create_meta.html', {"form" : form} )
