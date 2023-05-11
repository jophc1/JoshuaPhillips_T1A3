from maze_generator import (generate_maze_ascii, current_moves, 
                           MazeIntRangeError, MazeDifficultyInputError)
import pytest

# both row and column integer inputs into generate_maze_ascii 
# must be from 10-30 otherwise a MazeIntRangeError is raised
def test_invalid_size_ranges():  
    with pytest.raises(MazeIntRangeError):
        # this will raise a MazeIntRangeError if row is less than 10
        generate_maze_ascii(9,10,"medium")

    with pytest.raises(MazeIntRangeError):
        # this will raise a MazeIntRangeError if column is less than 10
        generate_maze_ascii(10,9,"medium")  

# difficulty string from user input must be either 'easy', 'medium' or 'hard'
# otherwise a MazeDifficultyError is raised
def test_wrong_difficulty():
    with pytest.raises(MazeDifficultyInputError):
        # not a difficulty, this will raise a MazeDifficultyError
        generate_maze_ascii(10,10,"impossible")

    with pytest.raises(MazeDifficultyInputError):
        # misspelled difficulty, this will raise a MazeDifficultyError
        generate_maze_ascii(10,10,"eas")  

# this is to test, when a new path step is being evaluated 
# to be added on to an existing path, that the
# current path step is being evaluated correctly to 
# determine what directions aren't blocked by either
# the boundry of the maze list or by the presence of adjacent paths
def test_correct_returned_moves():
    test_maze = [[0,0,0],[1,2,0],[0,0,0]]
    # this should only return 'up','right' and 'down' in moves list
    moves = current_moves(1,1,test_maze) 
    assert 'up' in moves and 'right' in moves and 'down' in moves and not 'left' in moves

    test_maze = [[0,0,0],[1,2,3],[0,0,0]]
    # this should only return 'up' and 'down' in moves list
    moves = current_moves(1,2,test_maze)  
    assert 'up' in moves and 'down' in moves and not 'right' in moves and not 'left' in moves