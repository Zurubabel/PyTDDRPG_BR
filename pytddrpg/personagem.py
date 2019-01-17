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
        if "vida" in atributos:
            self.__vida__ = atributos["vida"]

        if "forca" in atributos:
            self.__forca__ = atributos["forca"]

        if "defesa" in atributos:
            self.__defesa__ = atributos["defesa"]

    def atacar(self):
        return self.__forca__

    def receber_dano(self, dano):
        self.__vida__ -= dano - (self.__defesa__ / 2)

    def retornar_vida_restante(self):
        return self.__vida__

    def set_vida(self, vida):
        self.__vida__ = vida

