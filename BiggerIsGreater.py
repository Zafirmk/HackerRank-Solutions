def biggerIsGreater(w):

    #Since we can replace the values in a list by indexing
    w = list(w)

    #If w is already in descending order, no answer can be returned
    if sorted(w, reverse=True) == w:
        return("no answer")

    #Iterate through string backwards, since the next biggest lexicographical string will most likely occur
    #by swaps at the end of the string
    #Eg w = "hefg"
    for i in range(len(w)-2,-1,-1):

        #Search for the first character that is less than it's previous character
        if w[i] < w[i+1]:

            #remainder_string is the rest of the string
            #remainder_string = fg
            remainder_string = w[i+1:]

            #remainder_string_greater stores only those characters from remainder_string that are less than w[i]
            #w[i] = e
            #remainder_string_greater = [f, g]
            remainder_string_greater = [remainder_string[x] for x in range(len(remainder_string)) if remainder_string[x] > w[i]]

            #Selects the minimum value from remainder_string_greater
            #As that is the value that when replaced will give the first lexographically bigger string
            toReplace = min(remainder_string_greater)

            #Index of the char to be replaced
            toReplaceIndex = remainder_string_greater.index(toReplace) + len(w[:i+1])

            #Replacing the characters
            w[i], w[toReplaceIndex] = toReplace, w[i]

            #Sorting the remaining half of the list so that the characters in lexographical order
            w = w[:i+1] + sorted(w[i+1:])


            return("".join(w))

