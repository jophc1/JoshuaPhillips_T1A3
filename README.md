### Term 1 Assignment 3 Josh Phillips - Procedually generated maze game

#### [Link to git repository](https://github.com/jophc1/JoshuaPhillips_T1A3)

#### Styling guide
PEP 8, [styling guide link here](https://peps.python.org/pep-0008/)

#### Features of Maze game

##### Feature 1: Random Generation of a maze
When this maze game application is ran, a set of parameters will be asked for from the User in the terminal. These parameters will be for the size of the row & columns of the maze, the complexity of the maze (choose from easy, medium or hard) and a name title for the maze (this is optional).   

This feature will be related to using these parameters provided by the user with a specially created algorithm that will use multiple procedures that will be responsible for the randomised correct path of the maze, the creating of fake paths and the establishment of start & end points for our maze. This algorithm will be be heavily relient on looping structures like for and while loops to reduce the amount of repeated code, will need to utilize error handling to check that the inputted parameters are valid or within the limits of the game, and will use functions to split up the algorithm into smaller manageable pieces to allow better code readability and debugging.

##### Feature 2: Terminal play of generated maze, single maze mode
This feature is based around one of the three gaming modes that is offered by our maze gaming application. This feature is for the traversal of our generated maze through the terminal by inputting certain keys, where our position in the maze can be represented by a cross (+). Our position will begin at the start point on the left part of the maze and will need to use inputs (e.g. using w,a,s,d to indicate direction) to navigate through maze till we hit the end, to where we win and asks us if we want to play another game.   

##### Feature 3: Terminal play of generated maze, multi-maze mode
This feature is for our second gaming mode, multi-maze mode. Multi-maze mode works the same ways as our single maze mode where we transverse from start to end, but in this mode we specify how many randomised mazes we wish to do in a row. An example is if we decide 3 mazes, our game starts on the first maze, we get to end of first maze and a second maze is generated, we navigate the second maze, our third maze is generated and when we finish our third maze, a time appears on how long it took to finish and asks it we want to play another game.

##### Feature 4: Output generated maze into a .txt file for a printable maze puzzle
This feature is for our third gaming mode, except its not for playing a maze through the application. Instead this mode is to generate a randomised maze, export it into a .txt file in the form of ASCII. By putting our maze as ASCII into a .txt file, we can print this out and enjoy our maze without needing to use a computer.   

This feature will require the use of file handling to print out our maze into a .txt file.

#### Implementation plan
[Link to trello board]()

#### Help Documentation
##### System & Hardware requirements

##### Required dependencies

##### Installation process

##### How to use application (including command line arguments)
