# A function to accept a list argument of only integers and return even numbers only

def even(array):
    if not(isinstance(array, list)): return("Error! Parameter must be a list")
    if not(bool(array)): return("Error! List can not be empty")
    for x in array:
        if not(isinstance(x, int)): return("Error! List must contain integers only")
    newList = []
    for x in array:
        if x%2 == 0:
            newList.append(x)
    return("Note! There is no even number in the given list" if not(bool(newList)) else newList)

