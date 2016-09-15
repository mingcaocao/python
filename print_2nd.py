my_list = [1,2,3,4,5,6]

def print_2nd(lst):
#   lst[::2]
#    lst[1::2]
#    lst[1:-4:2]
#    lst[y_start:my_end]
    for num in range(1, len(my_list), 2):
        print lst[num]
