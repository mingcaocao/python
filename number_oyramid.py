def number_pyramid(num):
    """returns a pyramid string of numbers where biggest/center number is n"""
    if num == 1 or num == 0:
        return str(num)
    smaller_pyramid = number_pyramid(num - 1)
    return smaller_pyramid + str(num) + smaller_pyramid
def break_up(n):
    if n < 10:
        print(n)
    else:
        print(n)
        break_up(n//10)
        print(n)
break_up(2016)

f = open("movies.txt")
line = f.readline()
print line
g = f.tell()
f.readlines()
f.seek(g)
line2 = f.readline()
f.close()
print line2

lst = [7,8,9,5,3,2,2]
i = 0
while True:
    print lst[i]
    i += 1
    if i == len(lst) - 1:
        break
    
