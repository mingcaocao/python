#write a func that computes the length of hypotenuse
#given the other 2 sides

#arguments to func - input to func



def calc_hypotenuse(a, b):
    '''
        calc hypo ...pytha
    '''
    #actual code - computes c

    import math
    c = math.sqrt(a ** 2 + b ** 2)

    return c

def main():
    a = input("Enter one side length: ")
    b = input("Enter the other side length: ")
    c = calc_hypotenuse(a, b)
    print c

if __name__ == '__main__':
    main()
