from django.shortcuts import render, redirect, get_object_or_404
from semanas.forms import MetaForm
from semanas.models import MetaObjetivo,Objetivo_Semana, Registro_diario
from datetime import date

# Create your views here.


def semanas(request):

    if request.method == "GET":

        siglas = ["S", "T", "Q", "Q", "S", "S", "D"]

        todas_metas = Objetivo_Semana.objects.all()

        contexto = {"todas_metas": todas_metas, "siglas": siglas}

        return render(request, "Semanas/home_semanas.html", contexto)


def toggle(request, id):

    meta = get_object_or_404(Objetivo_Semana, id=id)
    

    registro, created = Registro_diario.objects.get_or_create(meta=meta)
    registro.marcar_hoje_como_feito()
    return redirect("metas")


def create_meta(request):

    if request.method == "POST":
        form = MetaForm(request.POST)

        form.save()

        return redirect("metas")

    else:

        form = MetaForm()

        return render(request, "Semanas/form_create_meta.html", {"form": form})
