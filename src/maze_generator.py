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
pprint(maze_paths)

# length of longest linear path from start to end point will be from one corner to another corner
path_length = (column_maze - 1) + (row_maze - 1) # This is length from top left corner of maze to bottom right corner

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

# While the path hasnt reached the end
while True:
    #Save the last position from prior loop as varibles
    last_row = current_row
    last_column = current_column
  
        # Check if we are next to an edge (left,right,top,bottom) and in a corner
    # left edge    
    if current_column == 0: 
        
        # top left corner
        if current_row == 0: 
            pass
            # next path cannot go left or up

        #bottom left corner    
        elif current_row == (row_maze - 1): 
            pass
            #next path cannot go left or down

        # left edge but not a corner   
        else: 
            pass
            #next path cannot go left

    #right edge, this column has exit on it        
    elif current_column == (column_maze - 1): 

        # end point 
        if current_row == end_point: 
            break #end loop by breaking out of while loop

        #top right corner
        elif current_row == 0: 
            pass
            #next path cannot go right or up

        #bottom right corner    
        elif current_row == (row_maze - 1): 
            pass
            #next path cannot go right or down

        # right edge but not a corner
        else: 
            pass
            #next path cannot go right, but also shouldn't go either up or down depending where the end point is located otherwise path may be stuck

    # top edge        
    elif current_row == 0: 
        pass
        #next path cannnot go up, but also shouldn't go left as it'll block path

    # bottom edge
    elif current_row == (row_maze - 1): 
        pass
        #next path cannot go down, but also shouldn't go left as it'll block path

    # not next to an edge or corner
    else: 
        pass
    
    # determine which direction last path came from, we can use this to restrict next path going 
    # back in that direction (eg if path went to right, then we dont want next path going left)
    if last_row == current_row:
        if last_column < current_column:
            restricted_direction = 'left'
        else:
            restricted_direction = 'right'
    else:
        if last_row < current_row:
            restricted_direction = 'top'
        else:
            restricted_direction = 'bottom'

    # After we make a new path, add one to current_path_index
    current_path_index += 1