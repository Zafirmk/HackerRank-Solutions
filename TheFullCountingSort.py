def countSort(arr):

    #Length of array
    n = len(arr)

    #Maximum value x
    maxval = int((max(arr))[0])

    #Midpoint of array
    halfway = n//2

    #Empty 2D array of length equal to maxval
    sortedarr = [[] for i in range(maxval+1)]

    #Final string to return
    toReturn = ""

    #Sorting the input array into sortedarr using the values of x
    #Iterates over arr, checks halfway condition and appends to respective index in sortedarr
    for count in range(n):
        val = int(arr[count][0])
        if count < halfway:
            sortedarr[val].append("-")
        else:
            sortedarr[val].append(arr[count][1])

    #Merging the words together from each list in sortedarr
    #Eg: ['-', 'that', 'is', 'the'] --> - that is the
    for i in range(0, len(sortedarr)):
        word = ""
        for j in range(0, len(sortedarr[i])):
            word += " "+str(sortedarr[i][j])
        toReturn += word

    #Using list slicing to remove the first " " ahead of the final string
    return(toReturn[1:len(toReturn)])

