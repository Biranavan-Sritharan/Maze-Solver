# Maze-Solver
Creating a programs that is able to traverse a maze from start point and reach an end point. New features are being added to my maze-solvers to get past certain situations.

The maze can also be changed really easily if needed to by changing numbers in the array:
## KEY:
- 0 = empty space/path that can be taken
- 1 = wall
- 2 = start point
- 3 = end point/finish line
- 5 = trail/the path maze-solver has taken
- 6 = wall collision, when the maze solver encounters a wall in its path its changes it to a 6 and then finds a different route

## maze-solver 1
This maze solver moves only right and when it encounters a wall will move one space back and one row down then carry on moving right. End points that are behind walls can not be solved or end points on the left side will have a 50/50 chance at getting there depending on maze layout.

## maze-solver 2
This maze-solver was more of a test run using try and except when reaching index errors.

## maze-solver 3
Can now handle dead ends in a maze, also looks for alternate routes when there is an intersection and stores these coordinates as a tuple.
