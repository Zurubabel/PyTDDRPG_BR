"""
    Três atributos:
        Força
        Defesa
        Vida

    Causar dano:
        * Força (+ random)
            Crítico
        Dano = Força - Arre.Cima(Defesa / 2)

"""

class Personagem():

    def __init__(self, atributos):
        self.__vida__ = atributos["vida"]
        self.__forca__ = atributos["forca"]

    def atacar(self):
        return self.__forca__

    def receber_dano(self, dano):
        self.__vida__ -= dano

    def retornar_vida_restante(self):
        return self.__vida__

    def set_vida(self, vida):
        self.__vida__ = vida

