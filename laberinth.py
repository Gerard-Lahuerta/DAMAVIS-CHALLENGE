class Cell(): 
    '''
    Represents de cells of the laberinth
    '''
    def __init__(self):
        self.rotate = True
        self.neighbors = []
        self.distance = 0
        self.visited = False

    def set_distance(self, dist):
        self.distance = dist
    
    def add_neighbor(self, cell_position):
        self.neighbors.append(cell_position)
    
    def change_rotate(self):
        self.rotate = False

    def update_cell(self):
        self.visited = True

    def get_neigbors(self):
        return self.neighbors



def CalcDistance(): 
    '''
    Calculates de Manhattan distance
    '''
    pass


def AStar(): 
    '''
    Runs AStar algorithm to find the shortest path
    '''
    pass


laberinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','#','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]

if __name__ == "__main__":
    pass