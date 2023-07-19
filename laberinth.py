class Cell(): 
    '''
    Represents de cells of the laberinth
    '''
    def __init__(self, type, x, y, upper_bound):
        self.type = type
        self.neighbors = []
        self.visited = False
        self.n_visited = 0
        self.moves = 0
        self.axis = "X"
        self.position = [x,y]
        self.estimated_distance = upper_bound

        self.path = []
    
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
    
    def update_n_visited(self):
        self.n_visited += 1
    
    def get_n_visited(self):
        return self.n_visited
    
    def rotate(self):
        if self.axis == "X":
            self.axis = "Y"
        else:
            self.axis = "X"
        self.update_n_visited()

    def get_position(self):
        return self.position
    
    def get_distance(self):
        return self.distance
    
    def set_visited(self):
        self.visited = True

    def set_estimated_distance(self, dist):
        self.estimated_distance = self.moves + dist

    def get_visited(self):
        return self.visited
    
    def get_moves(self):
        return self.moves
    
    def set_moves(self, moves):
        self.moves = moves
    
    def get_estimate_distance(self):
        return self.estimated_distance
    
    def set_rotation(self, rot):
        self.axis = rot

    def get_rotation(self):
        return self.axis
    
    def get_type(self):
        return self.type


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

    upper_bound = (n_last_col+1)*n_last_row

    for n_row, row in enumerate(laberinth):
        for n_col, col in enumerate(row):
            cell = Cell(col, n_row, n_col, upper_bound)
            pos = [n_row, n_col]

            neigh = calc_cross_neighbors(pos, n_last_row, n_last_col)

            cell.set_neighbors(neigh)
            cell.set_estimate_distance = float("inf")

            laberinth[n_row][n_col] = cell

def possible_rotation_cells(pos, n_last_row, n_last_col):
    
    neighs = laberinth[pos[0]][pos[1]].get_neighbors()
    neighs += calc_vertice_neighbors(pos, n_last_row, n_last_col)

    if len(neighs) != 8:
        return False

    for j in neighs:
        t = laberinth[j[0]][j[1]].get_type()
        if t == "#":
            return False

    return True


############################################################################################


def conditions_needed(cell, neigh, neigh_pos, n_last_row, n_last_col, dist):
    if neigh.get_visited():
        return False

    if neigh.get_type() == "#":
        return False

    print(cell.get_rotation())

    if cell.get_rotation() == "X":
        if neigh_pos[1]+1 > n_last_col or neigh_pos[1]-1< 0:
            return False

        if "#" in [laberinth[neigh_pos[0]][neigh_pos[1]+1].get_type(), laberinth[neigh_pos[0]][neigh_pos[1]-1].get_type()]:
            return False
    else:
        if neigh_pos[0]+1> n_last_row or neigh_pos[0]-1< 0:
            return False
        if "#" in [laberinth[neigh_pos[0]+1][neigh_pos[1]].get_type(), laberinth[neigh_pos[0]-1][neigh_pos[1]].get_type()]:
            return False

    if cell.get_moves() + dist + 1 > neigh.get_estimate_distance():
        return False   
    
    return True

def expand(cell, pos_exit, n_last_row, n_last_col):

    add_to_queue = []

    for neigh_pos in cell.get_neighbors():
        neigh = laberinth[neigh_pos[0]][neigh_pos[1]]
        pos = cell.get_position()
        dist = calc_Manh_distance(pos, pos_exit)
        
        if conditions_needed(cell, neigh, neigh_pos, n_last_row, n_last_col, dist):    
            neigh.set_moves(cell.get_moves() + 1)
            neigh.set_estimated_distance(dist)
            neigh.set_rotation(cell.get_rotation())
            neigh.path = cell.path
            neigh.path.append(cell.position)

            add_to_queue.append(neigh)
    
    return add_to_queue

def A_Star(start, n_last_row, n_last_col): 
    '''
    Runs AStar algorithm to find the shortest path
    '''

    pos_exit = [n_last_row, n_last_col]
    queue = [start]

    while len(queue) != 0: # and count < 10:
        cell = queue[0]
        queue = queue[1:]
        cell.set_visited()

        pos = cell.get_position()
        if calc_Manh_distance(pos, pos_exit) == 1:
            print(cell.path)
            return cell.get_moves()
        
        queue += expand(cell, pos_exit, n_last_row, n_last_col)

        if possible_rotation_cells(pos, n_last_row, n_last_col):
            cell.rotate()
            queue += expand(cell, pos_exit, n_last_row, n_last_col)

        queue.sort(key=lambda c: c.estimated_distance, reverse = True)


        print(len(queue))
        l = []
        for i in queue:
            l.append(i.position)
        print(l)
        
        

    return -1


############################################################################################

laberinth = [ [".",".",".",".",".",".",".",".",".","."],
              [".","#",".",".",".",".","#",".",".","."],
              [".","#",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".","#",".",".",".",".",".",".",".","."],
              [".","#",".",".",".","#",".",".",".","."],
              [".",".",".",".",".",".","#",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","." ]]

'''
laberinth =[ [".",".","."],
             [".",".","."],
             [".",".","."] ]
'''
'''
laberinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','#','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]
'''
'''
laberinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','.','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]
'''

if __name__ == "__main__":

    n_last_row = len(laberinth)-1
    n_last_col = len(laberinth[-1])-1

    create_laberinth_cell(n_last_row, n_last_col)

    for i in laberinth:
        line = []
        for j in i:
            line.append(j.type)
        print(line)

    print(A_Star(laberinth[0][1], n_last_row, n_last_col))

