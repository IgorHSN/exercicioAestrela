class Adjacente:
    def __init__(self, cidade, custo):
        self.cidade = cidade
        self.custo = custo
        self.distancia_aestrela = cidade.distancia_linha_reta + self.custo
        