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
    return sum(pos_exit)-sum(pos)

def calc_cross_neighbors(pos, n_last_row, n_last_col):
    neighs = []

    for i in ([1,0],[-1,0],[0,1],[0,-1]):
            X = pos[0]+i[0]
            Y = pos[1]+i[1]
            if X > n_last_row or X < 0 or Y > n_last_col or Y < 0:
                continue
            neighs.append([X,Y])
    return neighs

def create_laberinth_cell(lab):
    n_last_row = len(lab)-1
    n_last_col = len(lab[-1])-1
    wall_pos = []

    pos_exit = [n_last_row, n_last_col]

    for n_row, row in enumerate(lab):
        for n_col, col in enumerate(row):
            cell = Cell(col)
            pos = [n_row, n_col]
            dist = calc_Manh_distance(pos, pos_exit)

            neigh = calc_cross_neighbors(pos, n_last_row, n_last_col)

            if col == "#":
                wall_pos.append(pos)

            cell.set_distance(dist)
            cell.set_neighbor(neigh)

            lab[n_row][n_col] = cell

    return lab, wall_pos


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
    laberinth, _ = create_laberinth_cell(laberinth)

    for i in laberinth:
        line = []
        for j in i:
            line.append(j.type)
        print(line)
    print(len(_))

