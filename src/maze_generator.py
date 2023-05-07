import random
from pprint import pprint

def restricted_move(prior_coordinates: tuple, current_coordinates: tuple) -> str:
        if prior_coordinates[0] == current_coordinates[0]:
            if prior_coordinates[1] < current_coordinates[1]:
                direction = 'left'
            else:
                direction = 'right'
        else:
            if prior_coordinates[0] < current_coordinates[0]:
                direction = 'up'
            else:
                direction = 'down'
        return direction

def current_moves(row_position: int, column_position: int, maze_paths_indexes: list, restrict_left: int = 1) -> list:
    valid_directions = []
    #Check left
    if column_position -1 >= 0 and not maze_paths_indexes[row_position][column_position - 1] and not restrict_left:
        valid_directions.append('left')
    #Check up
    if row_position - 1 >= 0 and not maze_paths_indexes[row_position - 1][column_position]:
        valid_directions.append('up')
    #Check right
    if column_position + 1 <= (len(maze_paths_indexes[0]) - 1) and not maze_paths_indexes[row_position][column_position + 1]:
        valid_directions.append('right')
    #Check down
    if row_position + 1 <= (len(maze_paths_indexes) - 1) and not maze_paths_indexes[row_position + 1][column_position]:
        valid_directions.append('down')
    #Check if all directions blocked
    if not len(valid_directions): # all direction blocks
        valid_directions.append('blocked')
    #return list of directions in could go in as a string list e.g ['left', 'up', 'down']
    return valid_directions

def assign_new_path_index(row_position: int, column_position: int, direction_list: list, current_index: int, maze_list: list):
    move_direction = direction_list[random.randint(0, len(direction_list) - 1)]

    if move_direction in 'left':
        column_position -= 1
    elif move_direction in 'up':
        row_position -= 1
    elif move_direction in 'right':
        column_position += 1
    else: #down
        row_position += 1
    maze_list[row_position][column_position] = current_index
    return row_position, column_position


# create a maze the size of provided parameters in rows and columns
# lets make row and column be 10 eg. 10x10 maze
row_maze = 10
column_maze = 10

maze_paths = [[0 for _ in range(column_maze)] for _ in range(row_maze)]
# print(maze_paths)

# Determine a random starting and end point on the left and right side of the maze
start_point = random.randint(0, row_maze - 1)
end_point = random.randint(0, row_maze - 1)

maze_paths[start_point][0] = 1
maze_paths[end_point][column_maze - 1] = 1
# pprint(maze_paths)

# Create a path using path_length to connect the start and end point. 
# Will need to use some randomized direction while creating path

    # from start point, decide which direction to go next on the path. This could
    # be to any random direction as long as its not where you came from and as long as 
    # this new path won't be blocked in.
current_row = start_point   # begin at start point
current_column = 0          #
current_path_index = 2 #index starts at 2 as start point is 1
restricted_direction = ""

# create a function to check a direction that 


# While the path hasnt reached the end
while True:
    #Save the last position from prior loop as varibles
    last_row = current_row
    last_column = current_column
    two_random_direction = random.randint(0, 1)
    three_random_direction = random.randint(0, 2)
        # Check if we are next to an edge (left,right,up,down) and in a corner
    # left edge    
    if current_column == 0: 
        # top left corner or bottom left corner
        if current_row == 0 or current_row == (row_maze - 1): 
            # next path cannot go left or up, also can't go right as path would be stuck if old path came from right
            # therefore only path is to go left
            current_column += 1
        # left edge but not a corner   
        else: 
            #next path cannot go left
            # check where last path came from
            if restricted_direction in 'up':
                # can only go down or right
                if not two_random_direction: # move down
                    current_row += 1
                else: #move right
                    current_column += 1
                
            elif restricted_direction in 'down':
                #can only go up or right
                if not two_random_direction: # move down
                    current_row -= 1
                else: #move right
                    current_column += 1
            #first path move of maze if not a corner
            else:
                if not three_random_direction: # move up
                    current_row -= 1
                elif three_random_direction == 1: # move right
                    current_column += 1
                else: # move down
                    current_row += 1

    #right edge, this column has exit on it        
    elif current_column == (column_maze - 1): 
        # end point 
        if current_row == end_point: 
            break #end loop by breaking out of while loop
        #up right corner
        elif current_row == 0: 
            #next path cannot go right or up, also cannot go left as this would block path
            # therefore can only go down
            current_row += 1
        #down right corner    
        elif current_row == (row_maze - 1): 
            #next path cannot go right or down, also cannot go left as this would block path
            #therefore can only go up
            current_row -= 1
        # right edge but not a corner
        else: 
            #next path cannot go right, but also shouldn't go either up or down depending where the end point is located otherwise path may be stuck
            # currently above end point
            if current_row < end_point:
                current_row += 1
            # currently below end point
            else:
                current_row -= 1

    # top edge and bottom edge        
    elif current_row == 0 or current_row == (row_maze - 1): 
        #next path cannnot go up, but also shouldn't go left as it'll block path, also can't go left as that will block path
        # therefore can only go right or down
        
        #if last step came from up or down, only go right
        if restricted_direction == 'down' or restricted_direction == 'up':
            current_column += 1
        # if top edge
        elif current_row == 0:
            if not two_random_direction:
                current_row += 1
            else:
                current_column += 1
        # if bottom edge
        else:
            if not two_random_direction:
                current_row -= 1
            else:
                current_column += 1
           
    # not next to an edge or corner
    else: 
        pass
        #check where last move came from
        if restricted_direction == 'up':
            # cannot go up or left
            #can go right or down
            if not two_random_direction: # move right
                current_column += 1
            else: # move down
                current_row += 1
            
        elif restricted_direction == 'left':
            # cannot go left
            #can go up, right or down
            if not three_random_direction: #move up
                current_row -= 1
            elif three_random_direction == 1:#move right
                current_column += 1
            else: #move down
                current_row += 1
        else:
            #cannot go down
            #can go right or up
            if not two_random_direction: # move right
                current_column += 1
            else: # move up
                current_row -= 1
    
    #assign current path index to next path
    maze_paths[current_row][current_column] = current_path_index

    # determine which direction last path came from, we can use this to restrict the next path going 
    # back in that direction (eg if path went to right, then we dont want next path going left)

    restricted_direction = restricted_move((last_row, last_column), (current_row, current_column))

    # After we make a new path, add one to current_path_index
    current_path_index += 1

# debugging, remove later: print out new maze_paths
pprint(maze_paths)
end_point_index = current_path_index - 1 # this is used for evaluating the end point when creating ascii maze

# generate fake paths around correct path

# easy mode has a miniumum of 2 fake paths + amount of columns of maze // 6
# medium does 2 fake paths + amount of columns of maze // 5
# hard does 2 fake paths + amount of columns of maze // 4

user_input_difficulty = 'hard' # this will be from terminal prompt, remember to lowercase actual input later
if user_input_difficulty in 'easy':
    fake_modifier = 6
elif user_input_difficulty in 'medium':
    fake_modifier = 5
else:
    fake_modifier = 4

fake_path_quantity = random.randint(column_maze // fake_modifier, (column_maze // fake_modifier) + 2)

# one fake path will be from 1-3 position of start point
# another fake path will be from 1-3 positions from end point
# all other fake paths will be from positions between these two fake paths starting points
fake_path_start = random.randint(1,3)
fake_path_end = random.randint(current_path_index - 3, current_path_index - 1)
fake_path_set = set([fake_path_start, fake_path_end])

while len(fake_path_set) < fake_path_quantity + 2:
    fake_path_set.add(random.randint(fake_path_start + 1, fake_path_end - 1))

fake_path_starting_points = list(fake_path_set)
fake_path_starting_points.sort()
print(fake_path_starting_points)

# Find starting point of fake path, evaluate if there can be a fake path generated from correct path
# if not continue to next fake path starting point else we can generate a fake path from it
correct_to_fake_connection = [] # this will contain a list of tuples that will have the indexes of correct path index and first step of fake path
for fake_starting_point in fake_path_starting_points:
    # find where this point is on correct path and get the row, column coordinates
    # find row and column
    for row_index in range(len(maze_paths)):
        if fake_starting_point in maze_paths[row_index]:
            current_row = row_index
            current_column = maze_paths[row_index].index(fake_starting_point)
            break
    print(current_row, current_column)

    # need a way to save first path index from fake path and associate it with correct path index so we can print out a clear spot for fake path
    next_path_direction = ""
    while True:
        # check if there is a valid path next to current point (i.e is there a spot left,right,up or down that is 0)
        current_path_index += 1 
        next_path_direction = current_moves(current_row, current_column, maze_paths, 0)
        if "blocked" in next_path_direction :
            break
        current_row, current_column = assign_new_path_index(current_row, current_column, next_path_direction, current_path_index, maze_paths)
        correct_to_fake_connection.append((fake_starting_point, current_path_index))

pprint(maze_paths)


        





# Now we start generating fake path, everytime checking where our last fake path came from (restricted_direction)
# and checking if we can move a certain direction.
# We keep going towards right hand side of maze until either we are either hit the right side of maze
# or cannot create a new step for fake path (i.e. no valid paths)

# After we finished with first fake path, we do the next fake path, starting from beginning where we evaluate and then create path

# When all paths are done, then we are ready to start saving walls for corridors into another list so we can print walls around corridors and maze 
# in ASCII format, with (+) at the start position


