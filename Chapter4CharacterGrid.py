#Chapter 4 Character Picture Grid problem
"""
Use two loops to print the following shape from
the supplied grid. 

..OO.OO..
.OOOOOOO.
.OOOOOOO.
..OOOOO..
...OOO...
....O....

Author: David A Brown
"""
"""
Grid is a list with 9 separate lists that contain 6 items. 
In order to solve this, it is recommended that a nested loops
be used.  
"""
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])): #Gives length of columns
    for j in range(len(grid)): #Gives length of rows
        print(grid[j][i],end='') #As loops iterates, adds value to [] 
    print('')
