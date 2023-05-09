from maze_generator import generate_maze_ascii, maze_to_stringList, MazeDifficultyInputError, MazeIntRangeError
import os
# USER INPUTS - implement later on

while True:
    try:
        row_maze = int(input("Enter in integer number for row size of maze (min 10, max 30): "))
        column_maze = int(input("Enter in integer number for column size of maze (min 10, max 30): "))
        user_input_difficulty = input("Difficulty of maze? (easy, medium or hard): ")
        maze, start_row, finish_row = generate_maze_ascii(row_maze, column_maze, user_input_difficulty)
    except ValueError:
        print("Row and column must be a integer input")
    except MazeIntRangeError:
        print("Row and column must be between 10 and 30")
    except MazeDifficultyInputError:
        print("Difficulty can only be 'easy','medium','hard'")
    else:
        break
    
game_state = 1
player_row = start_row
player_column = 0
while game_state: #keep goin until player wins game
    os.system('cls' if os.name == 'nt' else 'clear') # use command "cls" if windoms os otherwuse use "clear" for unix os
    maze_string_list = maze_to_stringList(maze) #this will be required for feature 4 .txt output
    for line in maze_string_list:
        print(line, end="")
    #check if won
    if player_column == len(maze[0]) - 1 and player_row == finish_row:
        # print out you have won
        print("You have won")
        break   
    while True:
        user_direction = input("Input direction(Left = a, Up = w, Right = d, Down = s) else type \"quit\" to exit: ")
        if user_direction in ['a', 'w', 'd', 's']:
            previous_row = player_row
            previous_column = player_column
            if user_direction in 'a' and player_column and maze[player_row][player_column - 1] == " ":
                    player_column -= 2
            elif user_direction in 'w' and player_row and maze[player_row - 1][player_column] == " ":
                    player_row -= 2
            elif user_direction in 'd' and player_column < len(maze[0]) - 1 and maze[player_row][player_column + 1] == " ":
                    player_column += 2
            elif user_direction in 's' and player_row < len(maze) - 1 and maze[player_row + 1][player_column] == " ":
                    player_row += 2
            else:
                 print("blocked")
                 continue
            maze[previous_row][previous_column] = " "
            maze[player_row][player_column] = "@"
            break
        elif user_direction in 'quit':
            game_state = 0
            break
        else:
            print("Incorrect input")
    # check if direction blocked, #check if otherwise move player

    


   