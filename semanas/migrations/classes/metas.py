class Metas():

    def __init__(self, nome_meta, meta_vezes_na_semana, feito_na_semana):
        self.nome_meta = nome_meta
        self.meta_vezes_na_semana = meta_vezes_na_semana
        self.feito_na_semana = feito_na_semana

    def desempenho_da_semana (self):
        self.meta_vezes_na_semana
        self.feito_na_semana

        porgentagem_feita = (100 * self.feito_na_semana) / self.meta_vezes_na_semana

    def __str__(self):
        return f"{self.nome_meta} - {self.vezes_na_semana} vezes por semana e foi feito {self.desempenho_da_semana}%" 
