from maze_generator import generate_maze_ascii, maze_to_stringList, MazeDifficultyInputError, MazeIntRangeError

# USER INPUTS - implement later on

while True:
    try:
        row_maze = int(input("Enter in integer number for row size of maze (min 10, max 30): "))
        column_maze = int(input("Enter in integer number for column size of maze (min 10, max 30): "))
        user_input_difficulty = input("Difficulty of maze? (easy, medium or hard): ")
        maze, start_row, end_row = generate_maze_ascii(row_maze, column_maze, user_input_difficulty)
    except TypeError:
        print("Row and column must be a integer input")
    except MazeIntRangeError:
        print("Row and column must be between 10 and 30")
    except MazeDifficultyInputError:
        print("Difficulty can only be 'easy','medium','hard'")
    else:
        break

# row_maze = 10
# column_maze = 20
# user_input_difficulty = 'hard' # this will be from terminal prompt, remember to lowercase actual input later

maze_string_list = maze_to_stringList(maze) #this will be required for feature 4 .txt output

for line in maze_string_list:
    print(line, end="")