from classes.vetorOrdenado import vetorOrdenado


class AEstrela:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.encontrado = False

    def buscar(self, atual):
        print('------------------')
        print('Atual: {}'.format(atual.nome))
        atual.visitado = True

        if atual == self.objetivo:
            self.encontrado = True
        else:
            vetor_ordenado = vetorOrdenado(len(atual.adjacentes))
            for adjacente in atual.adjacentes:
                if adjacente.cidade.visitado == False:
                    adjacente.cidade.visitado = True
                    vetor_ordenado.insere(adjacente)
            vetor_ordenado.imprime()

            if vetor_ordenado.valores[0] != None:
                self.buscar(vetor_ordenado.valores[0].cidade)
