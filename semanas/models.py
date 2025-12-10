from django.db import models
from django.utils import timezone
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Registro(models.Model):
    dia_da_semana = models.CharField(max_length=50, blank=True, null=True)
    registro = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True


class Objetivo(models.Model):
    nome = models.CharField(max_length=100)
    concluida = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Objetivo_Semana(Objetivo):
    vezes_na_semana = models.IntegerField()
    feitas_na_semana = models.IntegerField(default=0)

    @property
    def progresso(self):
        if self.vezes_na_semana == 0:
            return 0
        return round((self.feitas_na_semana * 100) / self.vezes_na_semana)

    # NOVO: Esse método prepara os dados para o seu HTML desenhar os checkboxes
    def lista_dias(self):
        registro = self.Registro_diario.first()

        # Valores padrão (caso não tenha registro)
        dados = {
            "segunda": False,
            "terca": False,
            "quarta": False,
            "quinta": False,
            "sexta": False,
            "sabado": False,
            "domingo": False,
        }

        # Se existir registro, pega os valores reais
        if registro:
            dados["segunda"] = registro.segunda
            dados["terca"] = registro.terca
            dados["quarta"] = registro.quarta
            dados["quinta"] = registro.quinta
            dados["sexta"] = registro.sexta
            dados["sabado"] = registro.sabado
            dados["domingo"] = registro.domingo

        # Retorna a lista formatada para o template
        return [
            {"sigla": "S", "feito": dados["segunda"]},
            {"sigla": "T", "feito": dados["terca"]},
            {"sigla": "Q", "feito": dados["quarta"]},
            {"sigla": "Q", "feito": dados["quinta"]},
            {"sigla": "S", "feito": dados["sexta"]},
            {"sigla": "S", "feito": dados["sabado"]},
            {"sigla": "D", "feito": dados["domingo"]},
        ]


class Registro_diario(Registro):
    meta = models.ForeignKey(
        Objetivo_Semana, on_delete=models.CASCADE, related_name="Registro_diario"
    )

    segunda = models.BooleanField(default=False)
    terca = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    quinta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)

    def marcar_hoje_como_feito(self):
        dia_atual_ingles = date.today().strftime("%A")

        mapa_dias = {
            "Monday": "segunda",
            "Tuesday": "terca",
            "Wednesday": "quarta",
            "Thursday": "quinta",
            "Friday": "sexta",
            "Saturday": "sabado",
            "Sunday": "domingo",
        }

        nome_do_campo = mapa_dias.get(dia_atual_ingles)

        if nome_do_campo:
            # 1. Pega valor atual
            valor_atual = getattr(self, nome_do_campo)

            # 2. Inverte
            novo_valor = not valor_atual
            setattr(self, nome_do_campo, novo_valor)

            # 3. Salva Registro
            self.save()

            # 4. Atualiza a Meta Pai
            self.atualizar_total_meta()

            return novo_valor

        return None

    def atualizar_total_meta(self):
        """Conta quantos dias estão marcados e atualiza a meta pai"""
        lista_dias = [
            self.segunda,
            self.terca,
            self.quarta,
            self.quinta,
            self.sexta,
            self.sabado,
            self.domingo,
        ]

        # Soma os True (True=1, False=0)
        total_feitos = sum(lista_dias)

        self.meta.feitas_na_semana = total_feitos
        self.meta.save()


class MetaObjetivo(models.Model):
    nome_meta = models.CharField(max_length=100)
    vezes_na_semana = models.IntegerField()
    feitas_na_semana = models.IntegerField(default=0)

    def __str__(self):
        return self.nome_meta


class RegistroSemana(models.Model):

    meta = models.ForeignKey(
        MetaObjetivo, on_delete=models.CASCADE, related_name="registros"
    )

    segunda = models.BooleanField(default=False)
    terca = models.BooleanField(default=False)
    quarta = models.BooleanField(default=False)
    quinta = models.BooleanField(default=False)
    sexta = models.BooleanField(default=False)
    sabado = models.BooleanField(default=False)
    domingo = models.BooleanField(default=False)

    data_inicio = models.DateField(default=timezone.now)
    concluido = models.BooleanField(default=False)

    class Meta:
        # Garante apenas um registro por meta por semana
        unique_together = ("meta", "data_inicio")
        ordering = ["-data_inicio"]

    @property
    def progresso_percentual(self):
        dias = [
            self.segunda,
            self.terca,
            self.quarta,
            self.quinta,
            self.sexta,
            self.sabado,
            self.domingo,
        ]
        total_concluido = sum(dias)
        return int((total_concluido / 7) * 100)


@receiver(post_save, sender=Objetivo_Semana)
def criar_registro_automatico(sender, instance, created, **kwargs):
    # 'created' é True apenas se for um novo registro. 
    # Se for apenas uma edição de uma meta existente, ele será False.
        if created:
         Registro_diario.objects.create(meta=instance)
