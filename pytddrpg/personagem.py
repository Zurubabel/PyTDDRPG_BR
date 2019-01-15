class Personagem():

    def __init__(self):
        self.__vida__ = 0

    def receber_dano(self, dano):
        self.__vida__ -= dano
        return self.__vida__

    def set_vida(self, vida):
        self.__vida__ = vida

