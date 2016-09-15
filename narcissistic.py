#check whether the number input is narcissistic or not
x = int(input("Enter an integer between 1 and 10000"
              "(decimal would be taken its integer part):\n"))
#check the number is within range or not
if x > 10000 or x < 1:
    print('Not valid input!')
#for the case of 10000
elif x // 10000 == 1:
    print('It is not narcissistic.')
#for the case of 4-digit number
elif x // 1000 > 0:
    s = ((x // 1000) ** 4 + ((x % 1000) // 100) ** 4
         + ((x % 100) // 10) ** 4 + (x % 10) ** 4)
    if s == x:
        print('It is narcissistic.')
    else:
        print('It is not narcissistic.')
#for the case of 3-digit number
elif x // 100 > 0:
    s = (x // 100) ** 3 + ((x % 100) // 10) ** 3 + (x % 10) ** 3
    if s == x:
        print('It is narcissistic.')
    else:
        print('It is not narcissistic.')
#for the case of 2-digit number
elif x // 10 > 0:
    s = (x // 10) ** 2 + (x % 10) ** 2
    if s == x:
        print('It is narcissistic.')
    else:
        print('It is not narcissistic.')
#for the case of 1-digit number69868
else:
    print('It is narcissistic but it is trival.')
