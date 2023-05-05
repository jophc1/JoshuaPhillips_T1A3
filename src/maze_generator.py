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
# Will need to use some randomized direction will creating path

    # from start point, decide which direction to go next on the path. This could
    # be to any random direction as long as its not where you came from and as long as 
    # this new path won't be blocked in.
current_row = start_point   # begin at start point
current_column = 0          #

# While the path hasnt reached the end
while True:
        # Check if we are next to an edge (left,right,top,bottom) and in a corner
    if current_column == 0: # left edge
        if current_row == 0: # top left corner
            pass
            # next path cannot go left or up
        elif current_row == (row_maze - 1): #bottom left corner
            pass
            #next path cannot go left or down
        else: # left edge but not top or bottom corner
            pass
            #next path cannot go left
    elif current_column == (column_maze - 1): #right edge, this column has exit on it
        if current_row == end_point: # we are on end point, end loop by breaking out of while loop
            break
        elif current_row == 0: #top right corner
            pass
            #next path cannot go right or up
        elif current_row == (row_maze - 1): #bottom right corner
            pass
            #next path cannot go right or down
        else: # right edge but not top or bottom corner
            pass
            #next path cannot go right
    elif current_row == 0: # top edge
        pass
    elif current_row == (row_maze - 1): # bottom edge
        pass
    else: # not next to an edge
        pass

    # After we make a new path, subtract one from path_length
    path_length -= 1