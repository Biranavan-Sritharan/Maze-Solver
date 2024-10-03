#2 is start point
#3 is end point
#1 is a wall
#0 is empty space that can be walked in
#5, with this we can see the path the maze solver has taken!
#6 when it hits a wall it changes the 1 to a 6

maze = [
    [1,1,1,1,1,1,1,1,1],
    [1,2,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,1],
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

print("starting row: " + str(found_start_row_count) + " starting col: " + str(found_start_col_count))
print(maze[found_start_row_count][found_start_col_count]) #checks if obtained coords are correct, this should output 2 on terminal


#variables used in below loop
row_count = found_start_row_count 
col_count = found_start_col_count
path_trail = 5
wall_check = 6
end_loop = 0
corner_check = 0

dead_end_new_path = 0 #alts between 1 and 0
alt_path = []

for row in maze:
    for col in row:

        if dead_end_new_path > 0:
            print("new pos")
            row_count = alt_path_row_coord
            col_count = alt_path_col_coord
            pos = maze[row_count][col_count]
            dead_end_new_path = 0
            del alt_path[dead_end_new_path]

        else:
            pos = maze[row_count][col_count]

        if pos == 2:
            print("start")
            col_count += 1

        if pos == 0 or pos == 5:
            maze[row_count][col_count] = path_trail #basically current pos but also trailed added to curretn pos
            print("space")

            possible_paths = 0

            #left pos path check, for now just variables declared
            left_row_count = row_count
            left_col_count = col_count - 1

            #above pos path check
            above_row_count = row_count - 1
            above_col_count = col_count
            if maze[above_row_count][above_col_count] == 0 or maze[above_row_count][above_col_count] == 0: #add 5 later mayb
                possible_paths += 1

            #below pos path check
            below_row_count = row_count + 1
            below_col_count = col_count
            if maze[below_row_count][below_col_count] == 0 or maze[below_row_count][below_col_count] == 0: #add 5 later mayb
                possible_paths += 1

            #right pos path check
            right_row_count = row_count
            right_col_count = col_count + 1
            if maze[right_row_count][right_col_count] == 0 or maze[right_row_count][right_col_count] == 0: #add 5 later mayb   ###the 'solver' goes right by default anyways so no append to alt_path here
                possible_paths += 1

            if possible_paths >= 2 and maze[above_row_count][above_col_count] == 0 or maze[above_row_count][above_col_count] == 0: #add 5 later mayb
                alt_path.append((above_row_count,above_col_count))
            
            if possible_paths >= 2 and maze[below_row_count][below_col_count] == 0 or maze[above_row_count][above_col_count] == 0: #add 5 later mayb
                alt_path.append((below_row_count,below_col_count))

            #dead end check (horizontal dead end)
            if maze[right_row_count][right_col_count] == 1 and maze[above_row_count][above_col_count] == 1 and maze[below_row_count][below_col_count] == 1:
                print("dead end")
                coords = alt_path[0]
                alt_path_row_coord = coords[0]
                alt_path_col_coord = coords[1]

                dead_end_new_path = 1
                if dead_end_new_path > len(alt_path):
                    dead_end_new_path = 0
                #also once pos moved to new coords REMOVE it from alt_path
                #move pos to one of the other coords from alt_path array

            #corner check, bottom right corner
            elif maze[right_row_count][right_col_count] == 1 and maze[below_row_count][below_col_count] == 1:
                print("bottom right corner")
                if maze[above_row_count][above_col_count] == 0:
                    row_count -= 1

            #vertical column from bottom right corner scenario
            elif (maze[right_row_count][right_col_count] == 1 or maze[right_row_count][right_col_count] == 6) and (maze[left_row_count][left_col_count] == 1 or maze[left_row_count][left_col_count] == 6):
                row_count -= 1

            else:
                col_count += 1

        if pos == 1 or pos == 6:
            print("wall")
            corner_check += 1
            maze[row_count][col_count] = wall_check
            col_count -= 1
            row_count += 1


        if pos == 3:
            print("Reached End Point!")
            end_loop = 1
            break

    if end_loop == 1:
        end_loop = 0
        break

print(alt_path)
for x in maze:
    print(x)



#so this maze solver just goes horizontally until it hits a wall then just moves down one row/level and back one space/column
#BUT it can NOT look behind walls, so a checkpoint behind a wall will never be found, still an issue
#BUT it can now get out of deadends without clipping thru walls AND finds alternate routes to use when a dead end is encountered

#NEXT PLAN, maybe???
# so if it cant find the checkpoints via horizontally
# then it back tracks along the path it has taken and looks vertically instead,
# so, reached a wall infront and below THEN, if above = 0 move up one column


#some updating array check
# print(maze[2][2])
# new = 5
# maze[2][2] = 5
# print(maze[2][2])