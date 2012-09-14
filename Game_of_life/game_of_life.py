def game_of_life_generator(seed):
    
    game = GameOfLife(seed)
    
    while True:
        yield game.tick()
    


class GameOfLife(object):
    def __init__(self, seed):
        self.alive_cells = seed
        
        
    def tick(self):
        next_generation = set()
        survivors = [cell for cell in self.alive_cells if self.live_neighbours_count(cell) in (2, 3)]
        for cell in self.alive_cells:
            for neighbour in self.dead_neighbours(cell):
                if self.live_neighbours_count(neighbour) == 3:
                    next_generation.add(neighbour)
        self.alive_cells = set.union(next_generation, set(survivors))
        return self.alive_cells
    
    def live_neighbours_count(self, cell):
        return len(self.live_neighbours(cell))
    
    def dead_neighbours(self, cell):
        return neighbours(cell) - self.live_neighbours(cell)
    
    def live_neighbours(self, cell):
        living_neighbours = set()
        for neighbour in neighbours(cell):
            if neighbour in self.alive_cells:
                living_neighbours.add(neighbour)
        return living_neighbours


def neighbours(cell):
    cell_neighbours = set()
    deltas = set([(-1, -1), (0, -1), (1, -1),
                  (-1,  0),          (1,  0),
                  (-1,  1), (0,  1), (1,  1)])
    x, y = cell
    for dx,dy in deltas:
        cell_neighbours.add((x + dx, y + dy))
    return cell_neighbours
        