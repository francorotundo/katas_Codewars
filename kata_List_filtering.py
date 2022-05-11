# In this kata you will create a function that takes a list of non-negative integers and strings 
# and returns a new list with the strings filtered out.

def filter_list(l):
    for i in range(len(l)-1, -1, -1):
        if type(l[i]) == type('x'):
            l.pop(i)
    return l