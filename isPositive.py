def isPositive(n):
    if type(n) is not int or type(n) is float:
        raise ValueError, 'only accepting intergers'
    if n > 0:
        return True
    return False
