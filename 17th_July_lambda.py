x = lambda a: a + b 
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(c))


x = lambda a : a + 10
print(x(5))


'''
(base) indrani.sarkar@HO-002-LP-00389 Python Basics - July % /usr/bin/python
3 "/Users/indrani.sarkar/Python Basics /Python Basics - July/17th_July_lambd
a.py"
Enter b : 3
Enter c : 283
286

'''
## this won't work here because in the lambda function i am taking no arguments
x = lambda : a + b 
print('\n')
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(c))

'''
Traceback (most recent call last):
  File "/Users/indrani.sarkar/Python Basics /Python Basics - July/17th_July_lambda.py", line 21, in <module>
    print(x(c))
TypeError: <lambda>() takes 0 positional arguments but 1 was given

'''

# Here i am defining three arguments, but passing only two, and getting results for two 

x = lambda a,b,c: a + b 
print('\n')
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(a,b,c))

## this can happen too 


x = lambda a,b: a + b 
print('\n')
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(a,b))