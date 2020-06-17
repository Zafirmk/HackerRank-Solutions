"""
Number of balls per container remains constant.
So if there exists a container for each type of ball, result will be possible
"""

def organizingContainers(container):
    #Sum of each row in container (ie: Balls per container)
    sumrow = [sum(i) for i in container]

    #Sum of each column in container (ie: Number of balls for each type)
    sumcol = [sum(i) for i in (list(zip(*container)))]

    #If there exists a unique container for a unique ball, return true
    if sorted(sumcol) == sorted(sumrow):
        return("Possible")
    else:
        return("Impossible")
