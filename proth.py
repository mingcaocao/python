#proth number table from 1 to 10000
#set initial condition
x = 1;
k = 2 * x -1;
n = 1;
N = k * (2 ** n) + 1;
#outer loop for k
while N <= 10000:
    #inner loop for n
    while N <= 10000:
        if 2 ** n > k:
            print N
        n += 1
        N = k * (2 ** n) + 1
    x += 1
    k = 2 * x -1
    n = 1
    N = k * (2 ** n) + 1
