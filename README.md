# Maze-Solver
Creating a programs that is able to traverse a maze from a start point and reach an end point. New features are being added to my maze-solvers to get past certain situations.

The maze can also be changed really easily if needed to by changing numbers in the array:
## KEY:
- 0 = empty space/path that can be taken
- 1 = wall
- 2 = start point
- 3 = end point/finish line
- 5 = trail/the path maze-solver has taken
- 6 = wall collision, when the maze solver encounters a wall in its path its changes it to a 6 and then finds a different route

### maze 1 and 2 txt files:
Just some files with some mazes I used during testing, maze-solver 6 can complete both of these and other mazes I made :)

## maze-solver 1
This maze solver moves only right and when it encounters a wall will move one space back and one row down then carry on moving right. End points that are behind walls can not be solved or end points on the left side will have a 50/50 chance at getting there depending on maze layout.

## maze-solver 2
This maze-solver was more of a test run using try and except when reaching index errors.

## maze-solver 3
Can now handle dead ends in a maze, also looks for alternate routes when there is an intersection and stores these coordinates as a tuple.

## maze-solver 4
Added the beginning pieces of the backtracking and also able to detect vertical dead ends!

## maze-solver 5
Can now find the end point with its checks and doesn't just pass it, ALSO can now backtrack and search basically every square if it needs to

## maze-solver 6
Fixed an issue where if the start area had a vertical wall next to it, it would terminate itself prematurely. Fixed this by fixing the try and except.
This maze solver should be able to solve 99% of mazes

Also I commented out a lot of debug print statements, so if you want to see the alternate coordinates array being added to to get a better sense
at how it works just ctrl + f and search for: print(alt_path). Theres also a bunch more print statements if you are intrested as well.
