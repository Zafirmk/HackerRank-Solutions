from collections import Counter

def isValid(s):

    #Dictionary of occurances of each character
    counts = Counter(s)

    #Seperate all the values from the counts dictionary
    vals = counts.values()

    #Count how many characters occured n times
    unique_vals = Counter(vals)

    #Condition matching
    if len(unique_vals) == 1:
        return("YES")
    elif (len(unique_vals) == 2) and (abs(list(unique_vals.keys())[0]-list(unique_vals.keys())[1]) == 1 or list(unique_vals.keys())[0] == 1 or list(unique_vals.keys())[1] == 1) and (list(unique_vals.values())[1] == 1 or list(unique_vals.values())[1] == 1):
        return("YES")
    else:
        return("NO")
