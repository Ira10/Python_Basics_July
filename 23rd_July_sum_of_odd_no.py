# We want to add all the odd integers between (and including) a and b

def sun_odd(a,b):
    c = 0
    for i in range (a, b + 1):
        if i % 2 != 0:
            c += i 
    return c 


a = int(input("Enter a  "))
b = int(input("Enter the b pls  "))

# print(sun_odd(a,b))

print('\n')

print(sun_odd(a,b)) ### printing is needed
