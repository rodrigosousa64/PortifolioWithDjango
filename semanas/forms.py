from django import forms
from semanas.models import Meta_model

class MetaForm(forms.ModelForm):

    class Meta:
        model = Meta_model

        fields = ['nome_meta' , 'vezes_na_semana']
