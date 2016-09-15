#check whether the number input is abundant or not
#Quite the same as the perfect program only with the change of condition
#set the initial condition
divisor = 1;
s = 0;
#check wheter the input number is in range or not
x = int(input("Enter an integer between 1 and 10000"
              "(decimal would be taken its integer part):\n"))
if x > 10000 or x < 1:
    print('Not valid input!')
#for the case of 1
elif x == 1:
    s = 0
#check the remain
else:
    while divisor < x:
        if x % divisor == 0:
            s = s + divisor
        divisor += 1
if s > x:
    print('It is abundant.')
else:
    print('It is not abundant.')
