import numpy as np


def findshortest(maze, path = [], shortest=None):
    if path == []:
        path = [(0, 0)]
    row, col = path[-1]
    if (row, col) == (Rows-1, Columns-1):
        if shortest == None or len(path) < len(shortest):
            shortest = path
        print("found", path)
        return shortest
    else:
        curr_path = path
        for next in [(row-1,col),(row+1,col),(row,col+1),(row,col-1)]:
            x, y = next
            if x < 0 or y < 0 or x > (Rows - 1) or y > (Columns - 1):
                continue
            elif next in path:
                continue
            elif maze[x][y] == 1:
                # print(next, "hit a wall")
                continue
            else:
                # here is the core part to avoid going to wrong direction
                # the initial / wrong code is like below, in which 'path' will be modified during 'for' loop
                # path = path + [next]
                curr_path = path + [next]
                # print(path)
                new_path = findshortest(maze, curr_path)
                if new_path != None:
                    shortest = new_path

    return shortest


# MAZE = [
# 0, 1, 0, 0, 0, 1,
# 0, 1, 0, 1, 0, 1,
# 0, 0, 0, 1, 0, 0,
# 0, 1, 1, 1, 1, 0
# ]
### Test test

Rows = 4
Columns = 7

MAZE = [
0, 1, 0, 0, 0, 0, 0,
0, 1, 0, 1, 0, 1, 0,
0, 0, 0, 1, 0, 1, 0,
0, 1, 1, 1, 1, 0, 0,
]



reshapedMaze = np.array(MAZE).reshape(Rows, Columns)
print(findshortest(reshapedMaze))

# listA = ['a','b','c','d']
#
# for i in range(len(listA)):
#     newlist = listA + [i]
#     print(newlist)
