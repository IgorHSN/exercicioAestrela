from classes.cidade import Cidade
from classes.Adjacente import Adjacente


class Grafo:
    Porto_Uniao = Cidade("Porto Uniao", 203)
    Paulo_Frontin = Cidade('Paulo Frontin', 172)
    Canoinhas = Cidade('Canoinhas', 141)
    Tres_Barras = Cidade('Tres Barras', 131)
    Sao_Mateus_do_Sul = Cidade('Sao Mateus do Sul', 123)
    Irati = Cidade('Irati', 139)
    Curitiba = Cidade('Curitiba', 0)
    Palmeira = Cidade('Palmeira', 59)
    Mafra = Cidade('Mafra', 94)
    Campo_Largo = Cidade('Campo Largo', 27)
    BaLsa_Nova = Cidade('Balsa Nova', 41)
    Lapa = Cidade('Lapa', 74)
    Tijucas_do_Sul = Cidade('Tijucas do Sul', 56)
    Araucaria = Cidade('Araucaria', 23)
    Sao_Jose_dos_Pinhais = Cidade('Sao Jose dos Pinhais', 13)
    Contenda = Cidade('Contenda', 35)

    Porto_Uniao.adiciona_adjacentes(Adjacente(Paulo_Frontin, 46))
    Porto_Uniao.adiciona_adjacentes(Adjacente(Canoinhas, 78))
    Porto_Uniao.adiciona_adjacentes(Adjacente(Sao_Mateus_do_Sul, 87))
    Paulo_Frontin.adiciona_adjacentes(Adjacente(Irati, 75))
    Paulo_Frontin.adiciona_adjacentes(Adjacente(Porto_Uniao, 46))
    Canoinhas.adiciona_adjacentes(Adjacente(Porto_Uniao, 78))
    Canoinhas.adiciona_adjacentes(Adjacente(Tres_Barras, 12))
    Canoinhas.adiciona_adjacentes(Adjacente(Mafra, 66))
    Tres_Barras.adiciona_adjacentes(Adjacente(Canoinhas, 12))
    Tres_Barras.adiciona_adjacentes(Adjacente(Sao_Mateus_do_Sul, 43))
    Sao_Mateus_do_Sul.adiciona_adjacentes(Adjacente(Porto_Uniao, 87))
    Sao_Mateus_do_Sul.adiciona_adjacentes(Adjacente(Tres_Barras, 43))
    Sao_Mateus_do_Sul.adiciona_adjacentes(Adjacente(Irati, 57))
    Sao_Mateus_do_Sul.adiciona_adjacentes(Adjacente(Lapa, 60))
    Sao_Mateus_do_Sul.adiciona_adjacentes(Adjacente(Palmeira, 77))
    Irati.adiciona_adjacentes(Adjacente(Paulo_Frontin, 75))
    Irati.adiciona_adjacentes(Adjacente(Sao_Mateus_do_Sul, 57))
    Irati.adiciona_adjacentes(Adjacente(Palmeira, 75))
    Mafra.adiciona_adjacentes(Adjacente(Canoinhas, 66))
    Mafra.adiciona_adjacentes(Adjacente(Lapa,57))
    Mafra.adiciona_adjacentes(Adjacente(Tijucas_do_Sul, 99))
    Tijucas_do_Sul.adiciona_adjacentes(Adjacente(Mafra, 99))
    Tijucas_do_Sul.adiciona_adjacentes(Adjacente(Sao_Jose_dos_Pinhais, 49))
    Sao_Jose_dos_Pinhais.adiciona_adjacentes(Adjacente(Tijucas_do_Sul, 49))
    Sao_Jose_dos_Pinhais.adiciona_adjacentes(Adjacente(Curitiba, 15))
    Curitiba.adiciona_adjacentes(Adjacente(Sao_Jose_dos_Pinhais, 15))
    Curitiba.adiciona_adjacentes(Adjacente(Araucaria, 37))
    Curitiba.adiciona_adjacentes(Adjacente(BaLsa_Nova, 51))
    Curitiba.adiciona_adjacentes(Adjacente(Campo_Largo,29))
    Campo_Largo.adiciona_adjacentes(Adjacente(Curitiba, 29))
    Campo_Largo.adiciona_adjacentes(Adjacente(BaLsa_Nova, 22))
    Campo_Largo.adiciona_adjacentes(Adjacente(Palmeira, 55))
    Palmeira.adiciona_adjacentes(Adjacente(Irati, 75))
    Palmeira.adiciona_adjacentes(Adjacente(Sao_Mateus_do_Sul, 77))
    Palmeira.adiciona_adjacentes(Adjacente(Campo_Largo, 55))
    Lapa.adiciona_adjacentes(Adjacente(Mafra,57))
    Lapa.adiciona_adjacentes(Adjacente(Sao_Mateus_do_Sul, 60))
    Lapa.adiciona_adjacentes(Adjacente(Contenda, 26))
    Contenda.adiciona_adjacentes(Adjacente(Lapa,26))
    Contenda.adiciona_adjacentes(Adjacente(BaLsa_Nova, 19))
    Contenda.adiciona_adjacentes(Adjacente(Araucaria, 18))
    Araucaria.adiciona_adjacentes(Adjacente(Contenda, 18))
    Araucaria.adiciona_adjacentes(Adjacente(Curitiba, 37))
    BaLsa_Nova.adiciona_adjacentes(Adjacente(Contenda, 19))
    BaLsa_Nova.adiciona_adjacentes(Adjacente(Curitiba,51))
    BaLsa_Nova.adiciona_adjacentes(Adjacente(Campo_Largo, 22))
