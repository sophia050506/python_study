def print_table(table):
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j].rjust(10), end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print_table(tableData)