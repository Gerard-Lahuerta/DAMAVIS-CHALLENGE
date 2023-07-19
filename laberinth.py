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
    
    def set_neighbors(self, neighbors_position):
        self.neighbors = neighbors_position

    def get_neighbors(self):
        return self.neighbors
    
    def change_rotate(self):
        self.rotate = False

    def update_cell(self):
        self.visited = True

    def get_neigbor(self):
        neigh = self.neighbors[self.n_visited//2]
        return neigh
    
    def get_n_visited(self):
        return self.n_visited


class Rectangle():
    '''
    Represents de rectangle to move in the laberinth
    '''
    def __init__(self):
        self.axis = "X"
        self.moves = 0

    def rotate(self):
        if self.axis == "X":
            self.axis = "Y"
        else:
            self.axis = "X"

    def update_move(self):
        self.moves += 1

    def clone(self):
        rect = Rectangle()
        rect.axis = self.axis
        rect.moves = self.moves


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

def calc_vertice_neighbors(pos, n_last_row, n_last_col):
    neighs = []
    for i in [1,-1]:
        for j in [1,-1]:
            X = pos[0]+i
            Y = pos[1]+j
            if X > n_last_row or X < 0 or Y > n_last_col or Y < 0:
                continue
            neighs.append([X,Y])
    return neighs


############################################################################################


def create_laberinth_cell(lab, n_last_row, n_last_col):
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
            cell.set_neighbors(neigh)

            lab[n_row][n_col] = cell

    return lab, wall_pos

def search_imposible_rotation_cells(lab, wall_pos, n_last_row, n_last_col):
    for i in wall_pos:
        neighs = lab[i[0]][i[1]].get_neighbors()
        neighs += calc_vertice_neighbors(i, n_last_row, n_last_col)
        for j in neighs:
            lab[j[0]][j[1]].change_rotate()

    return lab


############################################################################################


def A_Star(): 
    '''
    Runs AStar algorithm to find the shortest path
    '''
    pass


############################################################################################


laberinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','#','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]

if __name__ == "__main__":

    n_last_row = len(laberinth)-1
    n_last_col = len(laberinth[-1])-1

    laberinth, wall_pos = create_laberinth_cell(laberinth, n_last_row, n_last_col)

    for i in laberinth:
        line = []
        for j in i:
            line.append(j.rotate)
        print(line)

    print(wall_pos)
    laberinth = search_imposible_rotation_cells(laberinth, wall_pos, n_last_row, n_last_col)

    for i in laberinth:
        line = []
        for j in i:
            line.append(j.rotate)
        print(line)

