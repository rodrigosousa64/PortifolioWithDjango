from django import forms

from semanas.models import Objetivo_Semana

class MetaForm(forms.ModelForm):

    class Meta:
        model = Objetivo_Semana

        fields = ["vezes_na_semana", "nome"]
