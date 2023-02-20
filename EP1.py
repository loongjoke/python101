Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

fullname='Somchai Rukchard'
name=fullname[:7]
lastname=fullname[-8:]
print(name)
Somchai
print(lastname)
Rukchard
print(len(name))
7
>>> print(len(fullname))
16
>>> age='65'
>>> print('My name is{},I am {} yrs old'.format(name,age))
My name isSomchai,I am 65 yrs old
>>> print('My name is {},I am {} yrs old'.format(name,age))
My name is Somchai,I am 65 yrs old
>>> print('My name is {0},I am {1} yrs old'.format(name,age))
My name is Somchai,I am 65 yrs old
>>> print('My name is {n},I am {a} yrs old'.format(n=name,a=age))
My name is Somchai,I am 65 yrs old
>>> print(f'My name is{name},I am {age} yrs old')
My name isSomchai,I am 65 yrs old
>>> print(f'My name is {name},I am {age} yrs old')
My name is Somchai,I am 65 yrs old
>>> print(fullname.lower())
somchai rukchard
>>> print(fullname.upper())
SOMCHAI RUKCHARD
>>> 
============== RESTART: C:/Users/adumu/Desktop/Python101/Hello.py ==============
Traceback (most recent call last):
  File "C:/Users/adumu/Desktop/Python101/Hello.py", line 1, in <module>
    Print('Hello')
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> 
============== RESTART: C:/Users/adumu/Desktop/Python101/Hello.py ==============
Traceback (most recent call last):
  File "C:/Users/adumu/Desktop/Python101/Hello.py", line 1, in <module>
    Print('Hello')
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> 
============== RESTART: C:/Users/adumu/Desktop/Python101/Hello.py ==============
Hello
Hello
Hello
Hello
Hello
Hello
