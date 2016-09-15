def listcrazy(lst):
    lst.sort()
    lst1 = lst
    lst1[0:1] = [12]
    lst1.sort()
lst = [13,5,6]
listcrazy(lst)
