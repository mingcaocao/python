def get_divisors(n):
    '''get all divisors of n. n is positive.'''
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    return lst
    #return [1,2,3,4,6,12]

def is_abundant(n):
    list_div = get_divisors(n)
    return sum(list_div) - n > n
