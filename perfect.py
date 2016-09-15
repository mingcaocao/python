#check whether the number input is perfect or not
divisor = 1;
s = 0;
x = int(input("Enter an integer between 1 and 10000"
              "(decimal would be taken its integer part):\n"))
#Check the input number valid or not
if x > 10000 or x < 1:
    print('Not valid input!')
#Consider the case of 1 first
elif x == 1:
    s = 0
#Test the remaining number
else:
    #test number from 1 to x
    while divisor < x:
        if x % divisor == 0:
            s = s + divisor
        divisor += 1
if s == x:
    print('It is perfect.')
else:
    print('It is not perfect.')
