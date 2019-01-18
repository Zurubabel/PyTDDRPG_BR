import unittest
from pytddrpg.personagem import Personagem


class TestPersonagem(unittest.TestCase):

    def setUp(self):
        self.atributos = {
            "vida": 10,
            "forca": 5,
            "defesa": 0
        }
        self.personagem = Personagem(self.atributos)

    def test_PersonagemRecebeAtributoVidaAtravesDeUmDicionario(self):
        atrubutosTeste = {
            "vida": 10
        }
        personagemTeste = Personagem(atrubutosTeste)
        self.assertEqual(personagemTeste.retornar_vida_restante(), atrubutosTeste["vida"])

    def test_PersonagemRetornaAtributosAtravesDoMetodoRetornarValorAtributo(self):
        self.assertEqual(self.personagem.retornar_valor_atributo("vida"), self.atributos["vida"])
        self.assertEqual(self.personagem.retornar_valor_atributo("forca"), self.atributos["forca"])
        self.assertEqual(self.personagem.retornar_valor_atributo("defesa"), self.atributos["defesa"])

    def test_PersonagemRecebeAtributoForcaAtravesDeUmDicionario(self):
        self.assertEqual(self.personagem.atacar(), self.atributos["forca"])


    def test_PersonagemRecebeDanoERetornaAVidaRestanteCalculada(self):
        self.personagem.set_valor_atributo(50, "vida")

        self.personagem.receber_dano(10)

        self.assertEqual(self.personagem.retornar_vida_restante(), 40)

    def test_PersonagemCausaDanoAOutroPersonagem(self):
        self.personagem.receber_dano(self.personagem.atacar())
        self.assertEqual(self.personagem.retornar_vida_restante(), (self.atributos["vida"] - self.atributos["forca"]))

    def test_PersonagemNaoRecebeDanoSeSuaDefesaForODobroDoAtaqueDoAtacante(self):
        atributosAtacante = {
            "forca": 5
        }
        personagemAtacante = Personagem(atributosAtacante)

        atributosDefensor = {
            "vida": 10,
            "defesa": 10
        }
        personagemDefensor = Personagem(atributosDefensor)

        personagemDefensor.receber_dano(personagemAtacante.atacar())

        self.assertEqual(personagemDefensor.retornar_vida_restante(), atributosDefensor["vida"])

    def test_PersonagemConstaraComoMortoSeSuaVidaForMenorOuIgualAZero(self):
        atributos = {
            "vida": 10
        }
        personagem = Personagem(atributos)

        personagem.receber_dano(11)

        self.assertEqual(personagem.esta_vivo(), False)

if __name__ == "__main__":
    unittest.main()