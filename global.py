course = 'CIT590'

def f1(var1):
    course = 'CIT592'
    return f2(course[3:], course[-1])

def f2(var2, var1):
    global course
    return course[3:] + var2 * int(var1)

def main():
    global course
    print f1(course)

if __name__ == '__main__':
    main()
