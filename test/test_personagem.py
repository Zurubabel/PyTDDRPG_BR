import unittest
from pytddrpg.personagem import Personagem


class TestPersonagem(unittest.TestCase):

    def test_PersonagemRecebeDanoERetornaAVidaRestanteCalculada(self):
        personagem = Personagem(50)
        personagem.receber_dano(10)

        self.assertEqual(personagem.retornar_vida_restante(), 40)

    def test_PersonagemCausaDanoAOutroPersonagem(self):
        personagemAtacante = Personagem(50, 5)

        personagemDefensor = Personagem(50)
        personagemDefensor.receber_dano(personagemAtacante.atacar())

        self.assertEqual(personagemDefensor.retornar_vida_restante(), 45)

if __name__ == "__main__":
    unittest.main()