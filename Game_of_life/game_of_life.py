def game_of_life_generator(seed):
    
    game = GameOfLife(seed)
    
    while True:
        yield game.tick()
    


class GameOfLife(object):
    def __init__(self, seed):
        self.alive_cells = seed
        
        
    def tick(self):
        self.alive_cells = set.union(self.births(), self.survivors())
        return self.alive_cells
    
    def survivors(self):
        return set([cell
                    for cell in self.alive_cells 
                    if len(self.live_neighbours(cell)) in (2, 3)])
    
    def births(self):
        births = set()
        for cell in self.alive_cells:
            births = set.union(births, set([neighbour 
                                           for neighbour in self.dead_neighbours(cell)
                                           if len(self.live_neighbours(neighbour)) == 3]))
        return births
    
    def dead_neighbours(self, cell):
        return neighbours(cell) - self.live_neighbours(cell)
    
    def live_neighbours(self, cell):
        return set([neighbour
                    for neighbour in neighbours(cell)
                    if neighbour in self.alive_cells])


def neighbours(cell):
    cell_neighbours = set()
    deltas = set([(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)])
    x, y = cell
    for dx,dy in deltas:
        cell_neighbours.add((x + dx, y + dy))
    return cell_neighbours
        