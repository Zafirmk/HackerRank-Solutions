import bisect

#Function to calculate median of a sorted list
def median(mylist,d,m):
    if d % 2 != 0:
        return(mylist[m])
    else:
        return(sum(mylist[m - 1:m + 1]) / 2)


def activityNotifications(expenditure, d):

    n = len(expenditure)

    #Midpoint of the list whose median is to be calculated
    m = d//2

    #Result to return
    notifs = 0

    #First set of d days in ascending order
    prev_expenditure = (sorted(expenditure[:d]))

    #Iterate from d to the end of the list
    #Because minimum number of days in prev_expenditure list is d 
    for i in range(d, n):

        #Median of prev_expenditure list
        result = median(prev_expenditure, d, m)

        #Check condition for notifications
        if expenditure[i] >= 2*result:
            notifs += 1

        #Find (from expenditure) the index which must be deleted in prev_expenditure
        del prev_expenditure[bisect.bisect_left(prev_expenditure,expenditure[i-d])]

        #Insert the new value (expenditure[i]) into prev_expenditure whilst still maintaining order
        bisect.insort(prev_expenditure, expenditure[i])
    return(notifs)

