spam = ['a', 'b', 'c', 'd']
for i in range(len(spam)):
    print("and",spam[i]) if i == len(spam) - 1 else print(spam[i],"," , end="")


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
row = len(grid[1])
col = len(grid)
print("row = %s,col = %s" % (row,col))
print("(3,0)",grid[3][0],"(0,3)",grid[0][3], "(8,0)",grid[8][0])
for i in range(len(grid)):
    for j in range(len(grid[i])):
        print(i,j)
        #print(grid[i][j], end="")
    print()