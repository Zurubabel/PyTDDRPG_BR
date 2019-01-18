"""
    Três atributos:
        Força
        Defesa
        Vida

    Causar dano:
        * Força (+ random)
            Crítico
        Dano = Força - Arre.Cima(Defesa / 2)

         if "vida" in atributos:
            self.__vida__ = atributos["vida"]
        else:
            self.__vida__ = 0

        if "forca" in atributos:
            self.__forca__ = atributos["forca"]
        else:
            self.__forca__ = 0

        if "defesa" in atributos:
            self.__defesa__ = atributos["defesa"]
        else:
            self.__defesa__ = 0


"""

class Personagem():

    def __init__(self, atributos):
       self.__atributos__ = atributos

    def retornar_valor_atributo(self, nome_atributo):
        if nome_atributo in self.__atributos__:
            return self.__atributos__[nome_atributo]
        else:
            return 0

    def atacar(self):
        return self.retornar_valor_atributo("forca")

    def receber_dano(self, dano):
        self.__vida__ -= dano - (self.retornar_valor_atributo("defesa") / 2)

    def retornar_vida_restante(self):
        return self.retornar_valor_atributo("vida")

    def set_vida(self, vida):
        self.__vida__ = vida

