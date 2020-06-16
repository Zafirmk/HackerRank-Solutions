def matrixRotation(matrix, r):
    m = len(matrix) #Rows
    n = len(matrix[0]) #Columns
    layers = min(m,n)//2 #Depth of matrix

    #Iterate over the matrix(Depth wise)
    for i in range(layers):
        currlayer = []

        for j in range(i, n-1-i):
            currlayer.append(matrix[i][j])
        for j in range(i, m-1-i):
            currlayer.append(matrix[j][n-1-i])
        for j in range(n-1-i, i, -1):
            currlayer.append(matrix[m-1-i][j])
        for j in range(m-1-i, i, -1):
            currlayer.append(matrix[j][i])

        #Number of different arrangements after rotating matrix
        variations = len(currlayer)

        #The minimum number of rotations required to reach positon at r
        shifts = r%variations

        #List slicing to rotate "matrix"
        currlayer = currlayer[shifts:]+currlayer[:shifts]

        #Index of element in the current layer/depth
        index = 0

        #Iterate over matrix and replace each value
        while index != len(currlayer):
            for j in range(i, n-1-i):
                matrix[i][j] = currlayer[index]
                index += 1
            for j in range(i, m-1-i):
                matrix[j][n-1-i] = currlayer[index]
                index += 1
            for j in range(n-1-i, i, -1):
                matrix[m-1-i][j] = currlayer[index]
                index += 1
            for j in range(m-1-i, i, -1):
                matrix[j][i] = currlayer[index]
                index += 1

    for row in matrix:
        print(*row)
