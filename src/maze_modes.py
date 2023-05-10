from maze_generator import generate_maze_ascii, maze_to_stringList, MazeDifficultyInputError, MazeIntRangeError
from os import system, name, path
from colored import fg, attr

class MazeFileOverwrite(Exception):
    pass

def user_input_maze_output():
    while True:
        try:
            row_maze = int(input("Enter in integer number for row size of maze (min 10, max 30): "))
            column_maze = int(input("Enter in integer number for column size of maze (min 10, max 30): "))
            user_input_difficulty = input("Difficulty of maze? (easy, medium or hard): ")
            return generate_maze_ascii(row_maze, column_maze, user_input_difficulty)
        except ValueError:
            print("Row and column must be a integer input")
        except MazeIntRangeError:
            print("Row and column must be between 10 and 30")
        except MazeDifficultyInputError:
            print("Difficulty can only be 'easy','medium','hard'")
            
def print_maze_and_move(maze, player_row, player_column, wall_colour = 1):
        
    system('cls' if name == 'nt' else 'clear') # use command "cls" if windoms os otherwise use "clear" for unix os
    maze_string_list = maze_to_stringList(maze) #this will be required for feature 4 .txt output
    print(f'{fg(wall_colour)}') # fg 1 is red, 2 is green, 13 is pink, 15 is white
    for line in maze_string_list:
        # print(line, end="")
        print(line, end="") 
    print(f'{attr(0)}') 
        # bg 20 blue 22 green 91 purple
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
            return player_row, player_column
        elif 'quit' == user_direction:
            raise KeyboardInterrupt
        else:
            print("Incorrect input")

def wall_colour_selection():
    colour_test_maze = ["_____", 
                        chr(0x256c) + " " + chr(0x256c) + " " + chr(0x256c), 
                        chr(0x256c) + " " + chr(0x256c) + " " + chr(0x256c), 
                        chr(0x256c) + " " + chr(0x256c) + " " + chr(0x256c), 
                        chr(0x203e) + chr(0x203e) + chr(0x203e) + chr(0x203e) + chr(0x203e)]
    while True:
        foreground_colour = input("What colour for maze walls? ('red','green','pink','white'): ")
        match foreground_colour:
            case 'red':
                colour_int = 1
            case 'green':
                colour_int = 2
            case 'pink':
                colour_int = 13
            case 'white':
                colour_int = 15
            case _:
                print("Invalid colour")
                continue
        system('cls' if name == 'nt' else 'clear') # use command "cls" if windoms os otherwise use "clear" for unix os
        print(f'{fg(colour_int)}') # fg 1 is red, 2 is green, 13 is pink, 15 is white
        for line in colour_test_maze:
            print(line) 
        print(f'{attr(0)}')
        while True:
            confirm_colour = input("Is this colour satisfactory? (yes/no): ")
            if "yes" == confirm_colour:
                return colour_int
            elif "no" == confirm_colour:
                break
            else:
                print("Invalid input ('yes' or 'no')")
       
def new_game():
    maze, start_row, end_row = user_input_maze_output()
    start_column = 0
    fg_int = wall_colour_selection()
    return maze, start_row, start_column, end_row, fg_int

def single_play_mode():
    maze, player_row, player_column, finish_row, fg_colour_int = new_game()

    while True: #keep goin until player wins game or quits
        if player_column == len(maze[0]) - 1 and player_row == finish_row: #reached end
            repeat_game = input("You have won, play again? (yes/no): ")
            if 'yes' == repeat_game:
                maze, player_row, player_column, finish_row, fg_colour_int = new_game()
            elif 'no' == repeat_game:
                raise KeyboardInterrupt
            else:
                print("Invalid input (input: 'yes' or 'no')")
                continue
        player_row, player_column = print_maze_and_move(maze, player_row, player_column, fg_colour_int)

def text_file_mode():
    # Prompt user for file name and check if valid
    try:
        while True:
            maze_name = input("Enter in name for maze file. No spaces and only alphabetic and numbers (e.g. 'maze1): ")
            if maze_name.isalnum():
                user_text_file = maze_name + '.txt'
                if path.exists(user_text_file): #file exists
                    while True:
                        confirm_maze_overwrite = input(f'{user_text_file} already exists, do you want to overwrite? (y/n): ')
                        if confirm_maze_overwrite == 'y':
                            raise MazeFileOverwrite
                        elif confirm_maze_overwrite == 'n':
                            break
                        else:
                            print("Invalid input 'y' or 'n' only")
                else:
                    break
            else:
                print("Name can only be alphabetic and numbers, no spaces")
    except MazeFileOverwrite:
        print(f'{user_text_file} will be overwritten with new maze')
    else:
        print(f'New file {user_text_file} will be created')
    
    # generate maze
    maze, _, _ = user_input_maze_output()
    #convert maze to string list
    mazeString_list = maze_to_stringList(maze)
    # put in file name from user into with open(userfile.txt, 'w')
    with open(user_text_file, 'w') as maze_file:
        for line in mazeString_list:
            maze_file.writelines(line)
    
    # when finished, raise KeyBoardException to exit program
    print(f'maze saved in {user_text_file}')
    raise KeyboardInterrupt