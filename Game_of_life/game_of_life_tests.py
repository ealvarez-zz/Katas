import unittest
from game_of_life import game_of_life_generator

class GeneratorTest(unittest.TestCase):
    
    def test_generator(self):
        seed = set()
        game = game_of_life_generator(seed)
        
        self.assertEqual(game.next(), set())
        
        
        
        
        





