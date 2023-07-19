class Cell(): 
    '''
    Represents de cells of the laberinth
    '''
    def __init__(self, type, x, y):
        self.type = type
        self.neighbors = []
        self.distance = 0
        self.visited = False
        self.n_visited = 0
        self.moves = 0
        self.axis = "X"
        self.position = [x,y]
    
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
    
    def rotate(self):
        if self.axis == "X":
            self.axis = "Y"
        else:
            self.axis = "X"

    def get_position(self):
        return self.position

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


def create_laberinth_cell(n_last_row, n_last_col):

    for n_row, row in enumerate(laberinth):
        for n_col, col in enumerate(row):
            cell = Cell(col, n_row, n_col)
            pos = [n_row, n_col]

            neigh = calc_cross_neighbors(pos, n_last_row, n_last_col)

            cell.set_neighbors(neigh)

            laberinth[n_row][n_col] = cell

def Possible_rotation_cells(pos, n_last_row, n_last_col):
    
    neighs = laberinth[i[0]][i[1]].get_neighbors(pos)
    neighs += calc_vertice_neighbors(pos, n_last_row, n_last_col)
    for j in neighs:
        t = laberinth[j[0]][j[1]].get_type()
        if t == "#":
            return False

    return True


############################################################################################


def A_Star(start, n_last_row, n_last_col): 
    '''
    Runs AStar algorithm to find the shortest path
    '''

    pos_exit = [n_last_row, n_last_col]
    queue = [start]

    for cell in queue:
        poss = cell.get_possition()
        if calc_Manh_distance(poss, pos_exit) == 1:
            return cell.get_moves()

    return None


############################################################################################


laberinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','#','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]

if __name__ == "__main__":

    n_last_row = len(laberinth)-1
    n_last_col = len(laberinth[-1])-1

    create_laberinth_cell(n_last_row, n_last_col)

    for i in laberinth:
        line = []
        for j in i:
            line.append(j.type)
        print(line)

