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
from copy import deepcopy

class Personagem():

    def __init__(self, atributos):
       self.__atributos__ = deepcopy(atributos)

    def retornar_valor_atributo(self, nome_atributo):
        if nome_atributo in self.__atributos__:
            return self.__atributos__[nome_atributo]
        else:
            return 0

    def atacar(self):
        return self.retornar_valor_atributo("forca")

    def receber_dano(self, dano):
        self.set_valor_atributo(
            self.retornar_valor_atributo("vida") - dano - (self.retornar_valor_atributo("defesa") / 2),
            "vida"
        )

    def esta_vivo(self):
        return self.retornar_valor_atributo("vida") > 0

    def retornar_vida_restante(self):
        return self.retornar_valor_atributo("vida")

    def set_valor_atributo(self, valor, atributo):
        self.__atributos__[atributo] = valor

