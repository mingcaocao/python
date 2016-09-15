Python 2.7.10 (default, Oct 23 2015, 18:05:06) 
[GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/Users/mingcao/Dropbox/python/forloopstring.py", line 1, in <module>
    s = abcdefghijklm
NameError: name 'abcdefghijklm' is not defined
>>> ================================ RESTART ================================
>>> 
a
b
c
d
e
f
g
h
i
j
k
l
m
>>> s = 'cit590 is happening right now'
>>> s[0]
'c'
>>> s[1]
'i'
>>> len(s)
29
>>> s[len(s)-1]
'w'
>>> s[len(s)]

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s[len(s)]
IndexError: string index out of range
>>> s[-1]
'w'
>>> s[-0]
'c'
>>> s[-len(s)]
'c'
>>> s
'cit590 is happening right now'

>>> s[2] = 's'

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s[2] = 's'
TypeError: 'str' object does not support item assignment
>>> s[1:4]
'it5'
>>> s[1:]
'it590 is happening right now'
>>> s[:5]
'cit59'
>>> s[1:-1]
'it590 is happening right no'
>>> True = 1
>>> 1 = True
SyntaxError: can't assign to literal
>>> True
1
>>> while true
SyntaxError: invalid syntax
>>> while True
SyntaxError: invalid syntax
>>> sqrt(2)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    sqrt(2)
NameError: name 'sqrt' is not defined
>>> math.sqrt(4)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    math.sqrt(4)
NameError: name 'math' is not defined
>>> import math
>>> math.sqrt(4)
2.0
>>> ================================ RESTART ================================
>>> 
>>> a=3, b=4
SyntaxError: can't assign to literal
>>> calc_hypotenuse(3,4)
5.0
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Enter one side length: 4
Enter the other side length: 5
>>> ================================ RESTART ================================
>>> 
>>> main()
Enter one side length: 1
Enter the other side length: 3
>>> ================================ RESTART ================================
>>> 
Enter one side length: 3
Enter the other side length: 4
>>> ================================ RESTART ================================
>>> 
Enter one side length: 4
Enter the other side length: 4

Traceback (most recent call last):
  File "/Users/mingcao/Dropbox/python/hypotenuse.py", line 27, in <module>
    main()
  File "/Users/mingcao/Dropbox/python/hypotenuse.py", line 24, in main
    print c
NameError: global name 'c' is not defined
>>> ================================ RESTART ================================
>>> 
Enter one side length: 3
Enter the other side length: 4
5.0
>>> ================================ RESTART ================================
>>> 
Enter one side length: 3
Enter the other side length: 4
None
>>> 
