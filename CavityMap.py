def cavityMap(grid):

    #Iterate over the grid, starting one away from the edge.
    #One away from the first row, upto the second last row
    for i in range(1, len(grid)-1):

        #One away from the first column, upto the second last column
        for j in range(1, len(grid[0])-1):

            #Current value
            val = (grid[i][j])
            
            #Check all four directions, if they meet the criteria given
            if (val > (grid[i+1][j])) and (val > (grid[i-1][j])) and (val > (grid[i][j+1])) and (val > (grid[i][j-1])):

                #Replace val with X, using string slicing
                #Note: replace() can't be used since it replaces all instances present
                grid[i] = grid[i][:j] + "X" + grid[i][j+1:]

    return(grid)