import unittest
from game_of_life import game_of_life_generator, GameOfLife

class GeneratorTest(unittest.TestCase):
    
    def test_generator(self):
        seed = set()
        game = game_of_life_generator(seed)
        
        self.assertEqual(game.next(), set())
        
        
    def test_blinker_several_generations(self):
        
        """
        ...
        ***
        ...
        
        ->
        
        .*.
        .*.
        .*.   

        """
        
        seed = set([(0,1),(1,1),(2,1)])
        
        game = game_of_life_generator(seed)
        
        self.assertEqual(game.next(), set([(1,0),(1,1),(1,2)]))
        self.assertEqual(game.next(), set([(0,1),(1,1),(2,1)]))
        

class GameOfLifeTest(unittest.TestCase):
    
    def test_tick(self):
        
        seed = set()
        game = GameOfLife(seed)
        
        self.assertEqual(game.tick(), set())





