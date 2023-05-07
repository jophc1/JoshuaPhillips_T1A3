import random
from pprint import pprint

def current_moves(row_position: int, column_position: int, maze_paths_indexes: list, restrict_left: int = 1) -> list:
    valid_directions = []
    #Check left - left not evaluated when correct path is being generated
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


# USER INPUTS - implement later on
row_maze = 10
column_maze = 10
user_input_difficulty = 'medium' # this will be from terminal prompt, remember to lowercase actual input later

# create a maze path indexes from user parameters (debugging - at the moment these are set values for row and column)
maze_paths = [[0 for _ in range(column_maze)] for _ in range(row_maze)]

# Determine a random starting and end point on the left and right side of the maze
start_point = random.randint(0, row_maze - 1)
end_point = random.randint(0, row_maze - 1)

maze_paths[start_point][0] = 1
current_row = start_point   # begin at start point coordinates
current_column = 0          #
current_path_index = 1 #index starts at 2 as start point is 1
next_path_direction = ""

# Correct path generation
while True:
    
    #check if right edge
    if current_column == (column_maze - 1):
        #on end point, therefore break loop
        if current_row == end_point:
            break
        # current position above end point
        elif current_row < end_point:
            next_path_direction = 'down'
        # current position below end point
        else:
            next_path_direction = 'up'
    else:
        next_path_direction = current_moves(current_row, current_column, maze_paths)
    current_path_index += 1
    current_row, current_column = assign_new_path_index(current_row, current_column, next_path_direction, current_path_index, maze_paths)
    
# debugging, remove later: print out new maze_paths
pprint(maze_paths) # DEBUGGING
end_point_index = current_path_index # this is used for evaluating the end point when creating ascii maze
print(end_point_index) # DEBUGGING

# generate fake paths around correct path
if user_input_difficulty in 'easy':
    fake_modifier = 6
elif user_input_difficulty in 'medium':
    fake_modifier = 5
else:
    fake_modifier = 4

fake_path_quantity = random.randint(column_maze // fake_modifier, (column_maze // fake_modifier) + 2) # total number of fake paths minus the compulsory two fake paths at start and end

fake_path_start = random.randint(1,3) # one fake path will be from 1-3 position of start point
fake_path_end = random.randint(current_path_index - 2, current_path_index) # another fake path will be from 1-3 positions from end point
fake_path_set = set([fake_path_start, fake_path_end]) # all other fake paths will be from positions between these two fake paths starting points

# keep generating random indexes until there are unique amount of indexes equal to total amount of fake paths
while len(fake_path_set) < fake_path_quantity + 2:
    fake_path_set.add(random.randint(fake_path_start + 1, fake_path_end - 1))

fake_path_starting_points = list(fake_path_set) #convert set to a list
fake_path_starting_points.sort() # sort fake path starting points
print(fake_path_starting_points) # DEBUGGING

correct_to_fake_connection = [] 
for fake_starting_point in fake_path_starting_points:
    # find where fake starting point is on the maze path index list
    for row_index in range(len(maze_paths)):
        if fake_starting_point in maze_paths[row_index]:
            current_row = row_index
            current_column = maze_paths[row_index].index(fake_starting_point)
            break
    print(current_row, current_column) # DEBUGGING
    # Fake path generation
    first_fake_step = 1
    while True:
        # check if there is a valid path next to current point (i.e is there a spot left,right,up or down that is 0)
        current_path_index += 1 
        next_path_direction = current_moves(current_row, current_column, maze_paths, 0)
        if "blocked" in next_path_direction :
            break
        current_row, current_column = assign_new_path_index(current_row, current_column, next_path_direction, current_path_index, maze_paths)
        if first_fake_step: # only want first fake step 
            correct_to_fake_connection.append((fake_starting_point, current_path_index))
            first_fake_step = 0

pprint(maze_paths) # DEBUGGING
print(correct_to_fake_connection) # DEBUGGING
# When all paths are done, then we are ready to start saving walls for corridors into another list so we can print walls around corridors and maze 
# in ASCII format, with (+) at the start position

## need variables:
# correct_to_fake_connection
# end_point_index
# maze_paths 

## create a list that will store the ASCII representation of maze
# will be (row size * 2) - 1 and (column size * 2) -1
maze_ascii = [[" " for _ in range((column_maze * 2) - 1)] for _ in range((row_maze * 2) - 1)]
test = 0
# check right and down on each item in column maze_paths except for last position where we only evaluate down (as right will be a wall)
# also last row will only check right as the bottom will be a wall

def evaluate_direction(row_position, column_position, direction, maze_index):
    if "right" in direction:
        pass
        if maze_index[row_position][column_position]: #there is a number here
            pass
        else: #there is no number here
            pass
        return chr(0x256c)
    elif "down" in direction:
        pass
        return chr(0x256c)
    else:
        raise Exception("Invalid direction string")


for row_index in range(row_maze):
        # test += 1
        for column_index in range(column_maze):
            if column_index <= column_maze - 2: # all columns except for last column
                # check right
                test = evaluate_direction(row_index, column_index, 'right', maze_paths)
                # save result into maze_ascii
                maze_ascii[(row_index * 2)][((column_index * 2) + 1)] = test

            if row_index <= row_maze - 2: # all rows except for last row 
                # check down
                test = evaluate_direction(row_index, column_index, 'down', maze_paths)

                maze_ascii[(row_index * 2) + 1][(column_index * 2)] = test

                if column_index <= column_maze - 2: # all except for bottom right corner
                    maze_ascii[(row_index * 2) + 1][(column_index * 2) + 1] = chr(0x256C)

    
## next need to evaluate each line of maze_paths where it check for either 0, a wall or a number
for _,col in enumerate(maze_ascii):
    print(col)



# if a zero, check right and down for either other zeroes or edge or a number. 
# if a number we check if number is less than equal to end_point_index, is so put a wall between zero and number
# if number is greater than end_point_index, 

# insert walls at the end so we know how many we need to put in


