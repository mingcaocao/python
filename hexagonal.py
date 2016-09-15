#check whether the number input is hexagonal or not
x = int(input("Enter an integer between 1 and 10000"
              "(decimal would be taken its integer part):\n"))
n = 1
if x > 10000 or x < 1:
    print('Not valid input!')
else:
    while 2*(n**2) - n <= x:
        if 2*(n**2) - n == x:
            print('It is hexagonal.')
            break
        n += 1
    if 2*(n**2) - n > x:
        print('It is not hexagonal.')
