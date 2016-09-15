#program to print a pattern of pluses based on user input number

#function does the above
def print_plus_pattern(input_pluses):
    '''
        prints a triangular plus pattern
        with input_pluses number of rows
    '''
    for x in range(1 , input_pluses + 1):
        s = ''
        for n in range(1 , x + 1):
            s = s + '+'
        print (s)
