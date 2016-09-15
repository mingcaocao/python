def recursive_replace_bar(lst):
    a = []
    if len(lst) == 0:
        return lst
    else:
        head = lst[0:1]
        if head[0] == "bar":
            head[0] = "foo"
        return head + recursive_replace_bar(lst[1:])


lst1 = ["bar", "l", "d", "bar", "k", "bar"]
a = recursive_replace_bar(lst1)
print a
