#check whether the number input is harshad or not
x = int(input("Enter an integer between 1 and 10000"
              "(decimal would be taken its integer part):\n"))
#check whether the number is within the range
if x > 10000 or x < 1:
    print('Not valid input!')
#for the case of 10000
elif x == 10000:
    print('It is harshad.')
#for the remain
else:
    s = (x // 1000) + ((x % 1000) // 100) + ((x % 100) // 10) + (x % 10)
    if x % s == 0:
        print('It is harshad.')
    else:
        print('It is not harshad.')
