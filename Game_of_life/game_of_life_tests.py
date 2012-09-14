import unittest
from game_of_life import game_of_life_generator, GameOfLife, neighbours

@unittest.SkipTest
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

    
    def test_tick_with_one_death(self):
        
        seed = set([(0,0)])
        game = GameOfLife(seed)
        
        game.tick()
        
        self.assertEqual(game.alive_cells, set())
    
    def test_live_neighbours_count(self):
        
        seed = set([(0, 0)])
        game = GameOfLife(seed)
        
        self.assertEqual(game.live_neighbours_count((0, 0)), 0)
    
    def test_live_neighbours_count_one_neighbours(self):
        seed = set([(0, 0), (0, 1)])
        game = GameOfLife(seed)
        
        self.assertEqual(game.live_neighbours_count((0, 0)), 1)
        self.assertEqual(game.live_neighbours_count((0, 1)), 1)


class NeighboursTest(unittest.TestCase):
    def test_neighbours_at_origin(self):
        cells_expected = set([(-1, -1), (0, -1), (1, -1),
                              (-1,  0),          (1,  0),
                              (-1,  1), (0,  1), (1,  1)])
        result = neighbours((0, 0))
        self.assertEqual(cells_expected, result)
        
    def test_neighbours(self):
        cells_expected = set([(0, 0), (1, 0), (2, 0),
                              (0, 1),         (2,  1),
                              (0, 2), (1, 2), (2,  2)])
        result = neighbours((1, 1))
        self.assertEqual(cells_expected, result)

if __name__ == '__main__':
    unittest.main()
    

