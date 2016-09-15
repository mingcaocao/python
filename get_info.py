def get_info(num):
    lst = []
    quotient = num / 5
    remainder = num % 5
    lst.append(quotient)
    lst.append(remainder)
    return lst

ans = get_info(31)
print "quot", ans[0]
print "rem", ans[1]
