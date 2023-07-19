class Cell(): 
    '''
    Represents de cells of the laberinth
    '''
    def __init__(self, type):
        self.type = type
        self.rotate = True
        self.neighbors = []
        self.distance = 0
        self.visited = False
        self.n_visited = 0

    def set_distance(self, dist):
        self.distance = dist
    
    def set_neighbor(self, neighbors_position):
        self.neighbors.append(neighbors_position)
    
    def change_rotate(self):
        self.rotate = False

    def update_cell(self):
        self.visited = True

    def get_neigbor(self):
        neigh = self.neighbors[self.n_visited//2]
        return neigh
    
    def get_n_visited(self):
        return self.n_visited

############################################################################################

def calc_Manh_distance(pos, pos_exit): 
    '''
    Calculates de Manhattan distance
    '''
    return sum(pos_exit-pos)

def calc_neighbors(pos, n_last_row, n_last_col):
    neighs = []
    for x,i in enumerate([1,-1]):
        for y,j in enumerate([1,-1]):
            X = pos[x]+i
            Y = pos[y]+j
            if X > n_last_row or X < 0 or Y > n_last_col or Y < 0:
                continue
            neighs.append([X,Y])
    return neighs

def create_laberinth_cell(lab):
    n_last_row = len(lab)-1
    n_last_col = len(lab[-1])-1

    pos_exit = [n_last_row, n_last_col]

    for n_row, row in enumerate(lab):
        for n_col, col in row:
            cell = Cell(col)
            pos = [n_row, n_col]
            dist = calc_Manh_distance(pos, pos_exit)

            neigh = calc_neighbors(pos, n_last_row, n_last_col)

            if col == "#":
                wall_neigh_pos += neigh


def A_Star(): 
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
    create_laberinth_cell(laberinth)