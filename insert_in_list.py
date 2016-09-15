my_list = [1,2,3,4,6]
def insert_in_list (lst, K, Value):
    lst.insert(K, Value)
    #K = 4
def main():
    insert_in_list(my_list, 4, 5)
    print my_list
if __name__ == "__main__":
    main()
