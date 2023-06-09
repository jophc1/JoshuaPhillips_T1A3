from random import randint

class MazeDifficultyInputError(Exception):
    pass

class MazeIntRangeError(Exception):
    pass

def current_moves(row_position, column_position, 
                  maze_paths_indexes, restrict_left = 1):
    valid_directions = []
    #Check left - left not evaluated when correct path is being generated
    if (column_position - 1 >= 0 and 
        not maze_paths_indexes[row_position][column_position - 1] and 
            not restrict_left):
        valid_directions.append('left')
    #Check up
    if (row_position - 1 >= 0 and 
        not maze_paths_indexes[row_position - 1][column_position]):
        valid_directions.append('up')
    #Check right
    if (column_position + 1 <= (len(maze_paths_indexes[0]) - 1) and 
        not maze_paths_indexes[row_position][column_position + 1]):
        valid_directions.append('right')
    #Check down
    if (row_position + 1 <= (len(maze_paths_indexes) - 1) and 
        not maze_paths_indexes[row_position + 1][column_position]):
        valid_directions.append('down')
    #Check if all directions blocked
    if not len(valid_directions): # all direction blocks
        valid_directions.append('blocked')
    #return list of directions in could go in as a string list e.g ['left', 'up', 'down']
    return valid_directions

def assign_new_path_index(row_position, column_position, 
                          direction_list, current_index, maze_list):
    move_direction = direction_list[randint(0, len(direction_list) - 1)]
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

def maze_to_stringList(maze_ascii_format):
    maze_string_list = []
    maze_string_list.append("".join(["_" for _ in range(len(maze_ascii_format[0]) + 2)]) + "\n") # top wall
    for _,maze_column in enumerate(maze_ascii_format):
        maze_string_list.append(chr(0x256c) + "".join(maze_column) + chr(0x256c) + "\n")
    maze_string_list.append("".join([chr(0x203e) for _ in range(len(maze_ascii_format[0]) + 2)]) + "\n") # bottom wall
    return maze_string_list

def build_wall_direction(direction):
    if "right" in direction:
        maze_character = chr(0x256c)
    else: 
        maze_character = chr(0x2550)
    return maze_character

def check_direction(maze_index_value, maze_next_value, 
                    direction, end_value, correct_fake_connection):    
    if maze_index_value: #there is a number here
        if (maze_index_value + 1 == maze_next_value 
            or maze_index_value - 1 == maze_next_value): 
            maze_character = " "
        elif ((maze_index_value, maze_next_value) in correct_fake_connection 
            or (maze_next_value, maze_index_value) in correct_fake_connection):
            maze_character = " "
        else:
            maze_character = build_wall_direction(direction)
    else: #there is no number here ie a zero
        if maze_next_value > end_value:
            maze_character = " "
        elif not maze_next_value: #chance to either build wall or keep open
            wall = randint(0,1)
            if not wall:
                maze_character = " "
            else:
                maze_character = build_wall_direction(direction)
        else:
            maze_character = build_wall_direction(direction)
    return maze_character

def evaluate_directions_and_assign(row_position, column_position, maze_index, 
                                   maze_final, end_value, correct_fake_connection):
    maze_value = maze_index[row_position][column_position]

    if column_position <= len(maze_index[0]) - 2: # all columns except for last column
        maze_next_value = maze_index[row_position][column_position + 1]
        maze_final[row_position * 2][(column_position * 2) + 1] = check_direction(maze_value, maze_next_value, 'right', 
                                                                                    end_value, correct_fake_connection)

    if row_position <= len(maze_index) - 2: # all rows except for last row
        maze_next_value = maze_index[row_position + 1][column_position]
        maze_final[(row_position * 2) + 1][column_position * 2] = check_direction(maze_value, maze_next_value, 'down', 
                                                                                    end_value, correct_fake_connection)
        if column_position <= len(maze_index[0]) - 2: # all except for bottom right corner of maze
                maze_final[(row_position * 2) + 1][(column_position * 2) + 1] = chr(0x256C)

def generate_maze_ascii(row_maze, column_maze, user_input_difficulty):

    available_difficulties = ["easy", "medium", "hard"]
    
    if row_maze < 10 or row_maze > 30 or column_maze < 10 or column_maze > 30:
        raise MazeIntRangeError

    if user_input_difficulty.lower() not in available_difficulties:
        raise MazeDifficultyInputError

    maze_paths = [[0 for _ in range(column_maze)] for _ in range(row_maze)]

    start_point = randint(0, row_maze - 1)
    end_point = randint(0, row_maze - 1)

    maze_paths[start_point][0] = 1
    current_row = start_point   
    current_column = 0          
    current_path_index = 1 

    # Correct path generation
    while True:
        if current_column == (column_maze - 1): #check if right edge
            if current_row == end_point: #on end point, therefore break loop
                break
            elif current_row < end_point:# current position above end point
                next_path_direction = 'down'
            else: # current position below end point
                next_path_direction = 'up'
        else: #not right edge
            next_path_direction = current_moves(current_row, current_column, maze_paths)
        current_path_index += 1
        current_row, current_column = assign_new_path_index(current_row, current_column, 
                                                            next_path_direction, current_path_index, 
                                                            maze_paths)
    # user inputted difficulty used to determine modifer used for fake path quantities
    if user_input_difficulty in 'easy':
        fake_modifier = 6
    elif user_input_difficulty in 'medium':
        fake_modifier = 5
    else: #hard
        fake_modifier = 4

    # total number of fake paths minus the compulsory two fake paths at start and end
    fake_path_quantity = randint(column_maze // fake_modifier, 
                                 (column_maze // fake_modifier) + 2) 
    # one fake path will be from 1-3 position of start point
    fake_path_start = randint(1,2)
    # another fake path will be from 3-5 positions from end point 
    fake_path_end = randint(current_path_index - 6, current_path_index - 4)
    # all other fake paths will be from positions between these two fake paths starting points 
    fake_path_set = set([fake_path_start, fake_path_end]) 

    # keep generating random indexes until there are unique amount of indexes equal to total amount of fake paths
    while len(fake_path_set) < fake_path_quantity + 2:
        fake_path_set.add(randint(fake_path_start + 1, fake_path_end - 1))

    fake_path_starting_points = list(fake_path_set) #convert set to a list
    fake_path_starting_points.sort() # sort fake path starting points
    correct_to_fake_connection = [] # contain where correct path and fake path should connect

    for fake_starting_point in fake_path_starting_points:
        # find where fake starting point is on the maze path index list
        for row_index in range(len(maze_paths)):
            if fake_starting_point in maze_paths[row_index]:
                current_row = row_index
                current_column = maze_paths[row_index].index(fake_starting_point)
                break

        # Fake path generation
        first_fake_step = 1
        while True:
            # check if there is a valid path next to current point (i.e is there a spot left,right,up or down that is 0)
            current_path_index += 1 
            next_path_direction = current_moves(current_row, current_column,
                                                 maze_paths, 0)
            if "blocked" in next_path_direction :
                break
            current_row, current_column = assign_new_path_index(current_row, current_column, 
                                                                next_path_direction, current_path_index, 
                                                                maze_paths)
            if first_fake_step: # only want first fake step 
                correct_to_fake_connection.append((fake_starting_point, current_path_index))
                first_fake_step = 0

    # create list to hold ascii maze
    maze_ascii = [[" " for _ in range((column_maze * 2) - 1)] for _ in range((row_maze * 2) - 1)]
    # evaluate and assigned ascii values to maze
    end_point_value = maze_paths[end_point][-1]
    for row_index in range(row_maze):
            for column_index in range(column_maze):
                evaluate_directions_and_assign(row_index, column_index, 
                                               maze_paths, maze_ascii, 
                                               end_point_value, correct_to_fake_connection)
                
    # input starting player position and end point (X)
    maze_ascii[start_point * 2][0] = '@' 
    maze_ascii[end_point * 2][-1] = 'X'
    #return maze ascii and row position of start and end point
    return maze_ascii, start_point * 2, end_point * 2   
    
