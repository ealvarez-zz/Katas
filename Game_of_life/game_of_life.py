def game_of_life_generator(seed):
    
    game = GameOfLife(seed)
    
    while True:
        yield game.tick()
    


class GameOfLife(object):
    def __init__(self, seed):
        self.alive_cells = seed
        
        
    def tick(self):
        return set()