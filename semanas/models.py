from django.db import models

# Create your models here.

class Meta_model(models.Model):
    nome_meta = models.CharField(max_length=100)
    vezes_na_semana = models.IntegerField()
    porgentagem_feita = models.FloatField(default = 0)

    def __str__(self):
        return self.nome_meta
