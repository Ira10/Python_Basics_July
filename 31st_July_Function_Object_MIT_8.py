from cmath import nan


def sum():
    sum_ = a + b 
    return sum_ 

a = 5
b = 6

print("\n")
print(sum())
print("\n")


print(type(sum()))

print("\n")


print(type(sum))

print("\n")


a = nan
type(a)

###########################

def is_even(i):
    return "yay" if i%2 == 0 else "Oh, sucks!" 

r = 2

pi = 22/7

my_func = is_even ## Not a FUNCTION CALL, JUST NAMES, no parenthesis nor parameters

a = is_even(3)

b = my_func(4)

print("\n")

print(a)

print("\n")

print(b)

print("\n")

################################ 

def calc(op,x,y):
    return op(x,y)

def add(a,b):
    return a + b 

def div(a,b):
    if b != 0:
        return a / b 
    print("Denominator was 0.")  # In your code, the print("Denominator was 0.") statement in the div function is designed to print a message if the denominator b is zero.


print("\n")

print(calc(add,2,3))

print("\n")

print(calc(div,24,2)) ## print denominator won't be back as return value is in inside and return value is returning

print("\n")

print(calc(div,24,0))

print("\n")


############################

def func_a():
    print("Inside function a")

def func_b(y):
    print("Inside function b")
    return y 

def funct_c(f,z):
    print("Inside function c")
    return f(z)

print("\n")


print(func_a())

print("\n")


print(5 + func_b(2))

print("\n")


print(funct_c(func_b,3))

print("\n")



######################### try #######################



def apply(criteria, n):
    count=0
    for i in range(n+1):
        if criteria(i):
            count+=1
    return count


def is_even(x):
    return x%2 == 0 

how_many = apply(is_even,10)

print(how_many)




