Python 2.7.10 (default, Oct 23 2015, 18:05:06) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/mingcao/Dropbox/python/dictionary.py", line 3, in <module>
    def get_value(dict, Key, msg=Name):
NameError: name 'Name' is not defined
>>> ================================ RESTART ================================
>>> 
>>> shopping
{'cookies': 6, 'apple': 7, 'orange': 1, 'pear': 4}
>>> lst = [1, 2, 3, 2, 5, 1]
>>> my_set = set(lst)
>>> my_set
set([1, 2, 3, 5])
>>> your_set = set([5,3,3,1,7,8])
>>> your_set
set([8, 1, 3, 5, 7])
>>> my_set.intersection(your_set)
set([1, 3, 5])
>>> my_set.union(your_set)
set([1, 2, 3, 5, 7, 8])
>>> 8 in my_set
False
>>> 8 in your_set
True
>>> my_set = my_set.intersection(your_set)
>>> my_set
set([1, 3, 5])
>>> 
