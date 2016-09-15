lst = [7,8,9,1]
lst = reduce(lambda x, y: [y] + x, lst, [])
lst
