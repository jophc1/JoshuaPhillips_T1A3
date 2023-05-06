import random
from pprint import pprint

# create a maze the size of provided parameters in rows and columns
# lets make row and column be 10 eg. 10x10 maze
row_maze = 10
column_maze = 10

maze_paths = [[0 for _ in range(column_maze)] for _ in range(row_maze)]
# print(maze_paths)

# Determine a random starting and end point on the left and right side of the maze
start_point = random.randint(0, row_maze - 1)
end_point = random.randint(0, column_maze - 1)

maze_paths[start_point][0] = 1
maze_paths[end_point][column_maze - 1] = 1
# pprint(maze_paths)

# length of longest linear path from start to end point will be from one corner to another corner
path_length = (column_maze - 1) + (row_maze - 1) # This is length from up left corner of maze to down right corner

    # add an amount to path_length depending on difficulty level
user_input_difficulty = 'medium' # this will be from terminal prompt, remember to lowercase actual input later
if user_input_difficulty in 'easy':
    path_length += (path_length - (path_length // 2))
elif user_input_difficulty in 'medium':
    path_length += (path_length - (path_length // 4))
elif user_input_difficulty in 'hard':
    path_length += path_length

# Create a path using path_length to connect the start and end point. 
# Will need to use some randomized direction while creating path

    # from start point, decide which direction to go next on the path. This could
    # be to any random direction as long as its not where you came from and as long as 
    # this new path won't be blocked in.
current_row = start_point   # begin at start point
current_column = 0          #
current_path_index = 2 #index starts at 2 as start point is 1
restricted_direction = None

# create a function to check a direction that 


# While the path hasnt reached the end
while True:
    #Save the last position from prior loop as varibles
    last_row = current_row
    last_column = current_column
  
        # Check if we are next to an edge (left,right,up,down) and in a corner
    # left edge    
    if current_column == 0: 
        # up left corner or down left corner
        if current_row == 0 or current_row == (row_maze - 1): 
            # next path cannot go left or up, also can't go right as path would be stuck if old path came from right
            # therefore only path is to go left
            current_column += 1
            maze_paths[current_row][current_column] = current_path_index
        # left edge but not a corner   
        else: 
            #next path cannot go left
            # check where last path came from
            if restricted_direction in 'right':
                pass
                #can only go up or down, but should check that there are no previous paths there
            elif restricted_direction in 'up':
                pass
                # can only go down or right
            elif restricted_direction in 'down':
                pass
                #can only go up or right

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
            maze_paths[current_row][current_column] = current_path_index
        #down right corner    
        elif current_row == (row_maze - 1): 
            #next path cannot go right or down, also cannot go left as this would block path
            #therefore can only go up
            current_row -= 1
            maze_paths[current_row][current_column] = current_path_index
        # right edge but not a corner
        else: 
            #next path cannot go right, but also shouldn't go either up or down depending where the end point is located otherwise path may be stuck
            # above end point
            if current_row < end_point:
                current_row += 1
            #below end point
            else:
                current_row -= 1

    # top edge         
    elif current_row == 0 or current_row == (row_maze - 1): 
        #next path cannnot go up, but also shouldn't go left as it'll block path, also can't go left as that will block path
        # therefore can only go right or down
        # this will determine right or up/down
        random_direction = random.randint(0, 1)
        #if last step came from up or down, only go right
        if restricted_direction == 'down' or restricted_direction == 'up':
            current_column += 1
            maze_paths[current_row][current_column] = current_path_index
        # if top edge
        elif current_row == 0:
            if not random_direction:
                current_row += 1
            else:
                current_column += 1
        # if bottom edge
        else:
            if not random_direction:
                current_row -= 1
            else:
                current_column += 1
           
    # not next to an edge or corner
    else: 
        pass
    
    # debugging, remove later: print out new maze_paths
    pprint(maze_paths)

    # determine which direction last path came from, we can use this to restrict the next path going 
    # back in that direction (eg if path went to right, then we dont want next path going left)
    if last_row == current_row:
        if last_column < current_column:
            restricted_direction = 'left'
        else:
            restricted_direction = 'right'
    else:
        if last_row < current_row:
            restricted_direction = 'up'
        else:
            restricted_direction = 'down'

    # After we make a new path, add one to current_path_index
    current_path_index += 1

    # do the logic for cases not next to edges

