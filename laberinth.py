class Cell(): 
    '''
    Represents de cells of the labyrinth
    '''
    def __init__(self, type, x, y, upper_bound):
        self.type = type
        self.neighbors = []
        self.moves = float("inf")
        self.axis = "X"
        self.position = [x,y]
        self.estimated_distance = upper_bound

        self.before = []
    
    def set_neighbors(self, neighbors_position):
        self.neighbors = neighbors_position

    def get_neighbors(self):
        return self.neighbors
    
    def rotate(self):
        if self.axis == "X":
            self.axis = "Y"
        else:
            self.axis = "X"
        self.moves += 1

    def get_position(self):
        return self.position

    def set_estimated_distance(self, dist):
        self.estimated_distance = self.moves + dist

    def get_moves(self):
        return self.moves
    
    def set_moves(self, moves):
        self.moves = moves
    
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
    return abs(sum(pos_exit)-sum(pos))

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


def create_labyrinth_cell(n_last_row, n_last_col):

    upper_bound = (n_last_col+1)*n_last_row

    for n_row, row in enumerate(labyrinth):
        for n_col, col in enumerate(row):
            cell = Cell(col, n_row, n_col, upper_bound)
            pos = [n_row, n_col]

            neigh = calc_cross_neighbors(pos, n_last_row, n_last_col)

            cell.set_neighbors(neigh)
            cell.set_estimate_distance = float("inf")

            labyrinth[n_row][n_col] = cell

def possible_rotation_cells(pos, n_last_row, n_last_col):
    
    neighs = labyrinth[pos[0]][pos[1]].get_neighbors()
    neighs += calc_vertice_neighbors(pos, n_last_row, n_last_col)

    if len(neighs) != 8:
        return False

    for j in neighs:
        t = labyrinth[j[0]][j[1]].get_type()
        if t == "#":
            return False

    return True


############################################################################################


def conditions_needed(cell, neigh, neigh_pos, n_last_row, n_last_col, dist):

    if neigh.get_type() == "#":
        return False

    if cell.get_rotation() == "X":
        if neigh_pos[1]+1 > n_last_col or neigh_pos[1]-1< 0:
            return False

        if "#" in [labyrinth[neigh_pos[0]][neigh_pos[1]+1].get_type(), labyrinth[neigh_pos[0]][neigh_pos[1]-1].get_type()]:
            return False
    else:
        if neigh_pos[0]+1> n_last_row or neigh_pos[0]-1< 0:
            return False
        if "#" in [labyrinth[neigh_pos[0]+1][neigh_pos[1]].get_type(), labyrinth[neigh_pos[0]-1][neigh_pos[1]].get_type()]:
            return False

    if cell.get_moves() + 1 > neigh.moves:
        return False   
    
    if calc_Manh_distance(cell.get_position(), neigh_pos) > 1:
        return False
    
    return True

def expand(cell, pos_exit, n_last_row, n_last_col, queue):

    add_to_queue = []

    for neigh_pos in cell.get_neighbors():
        neigh = labyrinth[neigh_pos[0]][neigh_pos[1]]
        pos = cell.get_position()
        dist = calc_Manh_distance(pos, pos_exit)
        
        if conditions_needed(cell, neigh, neigh_pos, n_last_row, n_last_col, dist):  
            neigh.set_moves(cell.get_moves() + 1)#+ calc_Manh_distance(pos, neigh_pos) )
            neigh.set_estimated_distance(dist)
            neigh.set_rotation(cell.get_rotation())
            neigh.before = cell.get_position()
            
            add_to_queue.append(neigh)
    
    return add_to_queue

def A_Star(start, n_last_row, n_last_col): 
    '''
    Runs AStar algorithm to find the shortest path
    '''

    start.set_moves(0)
    pos_exit = [n_last_row, n_last_col]
    queue = [start]

    while len(queue) != 0: # and count < 10:
        cell = queue[0]
        queue = queue[1:]

        pos = cell.get_position()
        if calc_Manh_distance(pos, pos_exit) == 1:
            return cell.get_moves()
        
        queue += expand(cell, pos_exit, n_last_row, n_last_col, queue)

        if possible_rotation_cells(pos, n_last_row, n_last_col):
            cell.rotate()
            queue += expand(cell, pos_exit, n_last_row, n_last_col, queue)

        queue.sort(key=lambda c: c.estimated_distance)#, reverse = True)

        '''
        print(len(queue))
        l = []
        for i in queue:
            l.append(i.position)
        print(l)
        '''
        
        

    return -1


############################################################################################
'''
labyrinth = [ [".",".",".",".",".",".",".",".",".","."],
              [".","#",".",".",".",".","#",".",".","."],
              [".","#",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".","#",".",".",".",".",".",".",".","."],
              [".","#",".",".",".","#",".",".",".","."],
              [".",".",".",".",".",".","#",".",".","."],
              [".",".",".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".",".",".","." ] ]
'''
'''
labyrinth =[ [".",".","."],
             [".",".","."],
             [".",".","."] ]
'''
'''
labyrinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','#','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]
'''

labyrinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','.','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]


if __name__ == "__main__":

    assert len(labyrinth) in range(3,1000), "ERROR: number of columns not accepted. Needs to be between 3 and 1000."
    assert len(labyrinth[-1]) in range(3,1000), "ERROR: number of rows not accepted. Needs to be between 3 and 1000."

    n_last_row = len(labyrinth)-1
    n_last_col = len(labyrinth[-1])-1

    create_labyrinth_cell(n_last_row, n_last_col)

    for i in labyrinth:
        line = []
        for j in i:
            line.append(j.type)
        print(line)

    print(A_Star(labyrinth[0][1], n_last_row, n_last_col))
    
    if len(labyrinth[-2][-1].before) != 0:
        cell = labyrinth[-2][-1]
    else :
        cell = labyrinth[-1][-2]
    print(cell.position)

    while len(cell.before) != 0:
        print(cell.before)
        cell = labyrinth[cell.before[0]][cell.before[1]]

