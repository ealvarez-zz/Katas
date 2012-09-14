def game_of_life_generator(seed):
    
    game = GameOfLife(seed)
    
    while True:
        yield game.tick()
    


class GameOfLife(object):
    def __init__(self, seed):
        self.alive_cells = seed
        
        
    def tick(self):
        survivors = set()
        for cell in self.alive_cells:
            if self.live_neighbours_count(cell) in (2, 3):
                survivors.add(cell)
        
        
        return set()
    def live_neighbours_count(self, cell):
        count = 0
        for neighbour in self.neighbours(cell):
            if neighbour in self.alive_cells:
                count +=1
        return count
    
    def neighbours(self, cell):
        cell_neighbours = set()
        deltas = set([(-1, -1), (0, -1), (1, -1),
                      (-1,  0),          (1,  0),
                      (-1,  1), (0,  1), (1,  1)])
        x, y = cell
        for dx,dy in deltas:
            cell_neighbours.add((x + dx, y + dy))
        return cell_neighbours
        