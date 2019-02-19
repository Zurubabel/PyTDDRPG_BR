import unittest
from pytddrpg.personagem import Personagem
from pytddrpg.arena import Arena


"""
    Controlar os personagens
        Os dois personagens em jogo (vc contra e o NPC)
    Verificar a integridade dos personagens
"""

class TestArena(unittest.TestCase):
    def test_ArenaInicializacao(self):
        npc = Personagem([])
        jogador = Personagem([])

        arena = Arena(jogador, npc)

        self.assertEqual(arena.exibirPersonagensNaArena(), "Personagem: Jailson; NPC: Josias")

if __name__ == '__main__':
    unittest.main()
