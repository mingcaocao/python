print "This program prints a multiplication table for even numbers only"

max_x = input("Enter a max value for x\n")
max_y = input("Enter a max value for y\n")
x = 1
#for x in range(1, max_x + 1)
#go from 1 to max_x
while (x <= max_x):
    y = 1
    while (y <= max_y):
        print str(x) + " * " + str(y) + " = " + str(x * y)
        #Increments y by 1 and then loops in inner loop
        y += 1
    #Increments x by 1 and then outer loops
    x += 1
