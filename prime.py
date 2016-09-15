#check whether the number input is prime or not
#if any integer between 1 and the input number itself is a divisor,
#the input number is not prime, vice versa. That's why I start the test from 2 not 1.
divisor = 2;
#check whether the input number in within the range and make the decimal become integer.
x = int(input("Enter an integer between 1 and 10000"
              "(decimal would be taken its integer part):\n"))
if x > 10000 or x < 1:
    print('Not valid input!')
#consider the case of 1 and 2 first
elif x == 1:
    print("1 is not prime.")
elif x == 2:
    print("2 is prime")
#test the remaining number
else:
    while divisor < x:
        if x % divisor == 0:
            print("It is not prime.")
            #end the loop when finding the divisor between 1 and the input number
            break
        divisor += 1
    #if the first divisor is the input number itself, that means it is prime
    if divisor == x:
        print 'It is prime.'
