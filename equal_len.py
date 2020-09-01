def equal_len(x, y):
    #Makes the length of two lists the same.
    while len(x) < len(y):
        x.append("NA")
    while len(y) < len(x):
        x.append("NA")
    return [x,y] #Returns a list of two lists.