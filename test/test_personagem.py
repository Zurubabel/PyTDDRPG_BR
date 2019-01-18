import unittest
from pytddrpg.personagem import Personagem


class TestPersonagem(unittest.TestCase):

    def test_PersonagemRetornaAtributosAtravesDoMetodoRetornarValorAtributo(self):
        atributos = {
            "vida": 11,
            "forca": 12,
            "defesa": 13
        }

        personagem = Personagem(atributos)

        self.assertEqual(personagem.retornar_valor_atributo("vida"), atributos["vida"])
        self.assertEqual(personagem.retornar_valor_atributo("forca"), atributos["forca"])
        self.assertEqual(personagem.retornar_valor_atributo("defesa"), atributos["defesa"])

    def test_PersonagemRecebeAtributoVidaAtravesDeUmDicionario(self):
        atributos = {
            "vida": 10
        }

        personagem = Personagem(atributos)
        self.assertEqual(personagem.retornar_vida_restante(), atributos["vida"])

    def test_PersonagemRecebeAtributoForcaAtravesDeUmDicionario(self):
        atributos = {
            "forca": 10
        }

        personagem = Personagem(atributos)
        self.assertEqual(personagem.atacar(), atributos["forca"])


    def test_PersonagemRecebeDanoERetornaAVidaRestanteCalculada(self):
        atributos = {
            "vida": 50
        }

        personagem = Personagem(atributos)
        personagem.receber_dano(10)

        self.assertEqual(personagem.retornar_vida_restante(), 40)

    def test_PersonagemCausaDanoAOutroPersonagem(self):
        atributos = {
            "vida": 50,
            "forca": 5
        }

        personagemAtacante = Personagem(atributos)

        personagemDefensor = Personagem(atributos)
        personagemDefensor.receber_dano(personagemAtacante.atacar())

        self.assertEqual(personagemDefensor.retornar_vida_restante(), 45)

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

if __name__ == "__main__":
    unittest.main()