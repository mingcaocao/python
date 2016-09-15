def sum(lst):
    s = 0
    for i in range(0, len(lst)):
        s += lst[i]
    return lst

def r_sum(lst):
    if len(lst ==1:):
        return lst[0]
    else:
        return lst[0] + r_sum(lst[1:])
