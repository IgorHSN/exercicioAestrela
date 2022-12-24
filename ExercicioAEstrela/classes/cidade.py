class Cidade:

    def __init__(self, nome, distancia_linha_reta):
        self.nome = nome
        self.visitado = False
        self.distancia_linha_reta = distancia_linha_reta
        self.adjacentes = []

    def adiciona_adjacentes(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacente(self):
        for i in self.adjacentes:
            print(i.cidade.nome)
