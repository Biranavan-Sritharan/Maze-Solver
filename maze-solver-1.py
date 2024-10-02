#2 is start point
#3 is end point
#1 is a wall
#0 is empty space that can be walked in
#5, with this we can see the path the maze solver has taken!
#6 when it hits a wall it changes the 1 to a 6

maze = [
    [1,1,1,1,1,1,1,1,1],
    [1,2,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,1],
    [1,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,3,1],
    [1,1,1,1,1,1,1,1,1]
]

#gets the starting coords, in this case 2 is starting pos in maze
start_row_count = 0
start_col_count = 0
found_start_row_count = 0
found_start_col_count = 0
for row in maze:
    # print(x)
    for col in row:
        # print(y)
        if start_col_count > len(row):
            start_col_count = start_col_count - len(row)
        if col == 2:
           found_start_col_count = start_col_count
           found_start_row_count = start_row_count
        start_col_count += 1
    start_row_count += 1

print("row: " + str(found_start_row_count) + " col: " + str(found_start_col_count))
print(maze[found_start_row_count][found_start_col_count]) #checks if obtained coords are correct

row_count = found_start_row_count 
col_count = found_start_col_count
path_trail = 5
end_loop = 0
for x in maze:
    for y in x:
        pos = maze[row_count][col_count]

        if pos == 2:
            print("start")
            col_count += 1

        if pos == 0 or pos == 5:
            maze[row_count][col_count] = path_trail
            print("space")
            col_count += 1

        if pos == 1 or pos == 6:
            print("wall")
            maze[row_count][col_count] = 6
            col_count -= 1
            row_count += 1

        if pos == 3:
            print("Reached End Point!")
            end_loop = 1
            break

    if end_loop == 1: #stops 'reached' being spammed
        break

for x in maze:
    print(x)

#so this maze solver just goes horizontally until it hits a wall then just moves down one row/level and back one space/column
#BUT it can NOT look behind walls, so a checkpoint behind a wall will never be found

#NEXT PLAN
# so if it cant find the checkpoints via horizontally
# then it back tracks along the path it has taken and looks vertically instead,
# so, reached a wall infront and below THEN, if above = 0 move up one column


#some updating array check
# print(maze[2][2])
# new = 5
# maze[2][2] = 5
# print(maze[2][2])