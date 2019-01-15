import unittest
from pytddrpg.personagem import Personagem


class TestPersonagem(unittest.TestCase):

    def test_PersonagemRecebeDanoERetornaAVidaRestanteCalculada(self):
        personagem = Personagem()
        personagem.set_vida(50)

        self.assertEqual(personagem.receber_dano(10), 40)

if __name__ == "__main__":
    unittest.main()