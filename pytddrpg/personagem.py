class Personagem():

    def __init__(self, vida):
        self.__vida__ = vida

    def atacar(self):
        return 5

    def receber_dano(self, dano):
        self.__vida__ -= dano

    def retornar_vida_restante(self):
        return self.__vida__

    def set_vida(self, vida):
        self.__vida__ = vida

