x = lambda a: a + b 
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(c))

'''
(base) indrani.sarkar@HO-002-LP-00389 Python Basics - July % /usr/bin/python3 "/Users/indrani
.sarkar/Python Basics /Python Basics - July/lambda_testing.py"
Enter b : 10
Enter c : 2
12
'''

## here c only getting transformed as a 

x = lambda a: a + 10 
# b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(c))   

'''
(base) indrani.sarkar@HO-002-LP-00389 Python Basics - July % /usr/bin/python3 "/Users/indrani.sarkar/Python Basics /Python Basics - July/lambda_testing.py"
Enter c : 23
33
'''

x = lambda a: a + 10 
# b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(x(5)) 

'''
(base) indrani.sarkar@HO-002-LP-00389 Python Basics - July % /usr/bin/python3 "/Users/indrani
.sarkar/Python Basics /Python Basics - July/lambda_testing.py"
Enter c : 7
15
''' 