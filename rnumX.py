def rnumX(str):
    if len(str) == 0:
        return 0
    elif str[0] == 'x':
        return 1 + rnumX(str[1:])
    else:
        return rnumX(str[1:])
