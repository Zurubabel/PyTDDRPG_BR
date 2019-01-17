import unittest
from pytddrpg.personagem import Personagem


class TestPersonagem(unittest.TestCase):

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
            "vida": 50
        }

        personagemAtacante = Personagem(atributos)

        personagemDefensor = Personagem(atributos)
        personagemDefensor.receber_dano(personagemAtacante.atacar())

        self.assertEqual(personagemDefensor.retornar_vida_restante(), 45)

if __name__ == "__main__":
    unittest.main()