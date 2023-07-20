'''
DAMAVIS CHALLENGE PROGRAM PROPORSAL

@Author: Gerard Lahuerta Martín
@Date: 20/07/2023

The program is separated in classes needed to run the search algorithm, auxiliar fucntions to calculate 
rellevant data, function that translate the input ( list(list(str)) ) into the structure needed to run the
search algorithm and the algorithm.

For more information about the algorithms and explanations of the decisions done while programming consult
the Readme file.
'''


###########################################################################################################


class Cell(): 
    '''
    Class Object that represents de cells of the labyrinth.

    It contains the rellevant information obtained in the input "labyinth map". 
    Also contains important information for the searching algorithm.

    Attributes:
      - type: character that represents the type of the cell (wall "#" or free ".").
      - neighbors: list of coordinates of its cells neighbors.
      - moves: integuer that count the moves done while its in the cell.
      - axis: character that represents the orientation of the rectangle (horizontal "X" or vertical "Y").
      - position: lest with the coordinates of the cell.
    '''
    def __init__(self, type, x, y, upper_bound):
        '''
        Inicialice the Cell class.

        Args:
          - type: character "#" or "." that represents the type of teh cell.
          - x: integuer which represents the row where the cell its found.
          - y: integuer which represents the column where the cell its found.
          - upper_bound: integuer which is the maximum number of moves that the rectangle could do.

        Rellevant information:
          - Attribute axis will be inicialiced in horizontal, "X".
          - Attribute moves will be inicialiced as infinite. 
        '''
        self.type = type
        self.neighbors = []
        self.moves = float("inf")
        self.axis = "X"
        self.position = [x,y]
        self.estimated_distance = upper_bound
    
    def set_neighbors(self, neighbors_position):
        '''
        Sets the new neighbors of the cell.

        Args:
          - neighbors_position: list with the coordinates of the new neighbors.
        '''
        self.neighbors = neighbors_position

    def get_neighbors(self):
        '''
        Returns the neighbors of the cell.
        '''
        return self.neighbors
    
    def rotate(self):
        '''
        Update the orientation of the rectangle that is in the cell.

        Rellevant information:
          - Rotate the rectangle is consider a moves, so the attribute moves will be increased in 1.
        '''
        if self.axis == "X":
            self.axis = "Y"
        else:
            self.axis = "X"
        self.moves += 1

    def get_position(self):
        '''
        Returns the position of the cell in the "labyrinth map".

        Return:
          - position: list
        '''
        return self.position

    def set_estimated_distance(self, dist):
        '''
        Updates the estimated moves needed to arribe at the exit.

        Args:
          - dist: integuer that represents the estimation of moves to complete the labyrinth.

        Rellevant information:
          - Is important to have the moves updated to register the real estimated distance.
        '''
        self.estimated_distance = self.moves + dist

    def get_moves(self):
        '''
        Returns the moves the rectangle have done to arribe at the cell.

        Return:
          - moves: integuer
        '''
        return self.moves
    
    def set_moves(self, moves):
        '''
        Set the new moves passed to the cell.

        Args:
          - moves: integuer that represents the new number of moves needed to arribe at the cell.
        '''
        self.moves = moves
    
    def set_rotation(self, rot):
        '''
        Set the new orientation of the rectangle that is the the cell.

        Args:
          - rot: character that represents the orientation of the rectangle.

        Rellevant information:
          - rot needs to be "#" or ".".
        '''
        self.axis = rot

    def get_rotation(self):
        '''
        Returns the orientation of the rectangle that is in the cell.

        Return:
          - axis: character
        '''
        return self.axis
    
    def get_type(self):
        '''
        Returns the type of the cell

        Return:
          - type: character
        '''
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


############################################################################################


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


def conditions_needed(cell, neigh, neigh_pos, n_last_row, n_last_col, dist):

    if neigh.get_type() == "#":
        return False

    if cell.get_rotation() == "X":
        if neigh_pos[1]+1 > n_last_col or neigh_pos[1]-1< 0:
            return False

        if "#" in [labyrinth[neigh_pos[0]][neigh_pos[1]+1].get_type(), 
                   labyrinth[neigh_pos[0]][neigh_pos[1]-1].get_type()]:
            return False
    else:
        if neigh_pos[0]+1> n_last_row or neigh_pos[0]-1< 0:
            return False
        if "#" in [labyrinth[neigh_pos[0]+1][neigh_pos[1]].get_type(), 
                   labyrinth[neigh_pos[0]-1][neigh_pos[1]].get_type()]:
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
            neigh.set_moves(cell.get_moves() + 1)
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
'''
labyrinth = [ ['.','.','.','.','.','.','.','.','.'],
              ['#','.','.','.','#','.','.','.','.'],
              ['.','.','.','.','#','.','.','.','.'],
              ['.','#','.','.','.','.','.','#','.'],
              ['.','#','.','.','.','.','.','#','.'] ]
'''

if __name__ == "__main__":

    assert len(labyrinth) in range(3,1000), "ERROR: number of columns not accepted. Needs to be between 3 and 1000."
    assert len(labyrinth[-1]) in range(3,1000), "ERROR: number of rows not accepted. Needs to be between 3 and 1000."

    n_last_row = len(labyrinth)-1
    n_last_col = len(labyrinth[-1])-1

    create_labyrinth_cell(n_last_row, n_last_col)

    print(A_Star(labyrinth[0][1], n_last_row, n_last_col))

