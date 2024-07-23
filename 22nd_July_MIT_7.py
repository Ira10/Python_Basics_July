# def is_even(i):
#     if i%2 == 0:
#         return True 
#     else:
#         return False
    


# is_even(3) ## this is not getting printed, bc it is just getting returned
# print(is_even(8))
# print(is_even(5))



############################## new #################################

# def is_even(i):
#     return i%2 == 0    

# is_even(3) ## this is not getting printed, bc it is just getting returned
# print(is_even(8))
# print(is_even(5))


############################## new exercise #################################

## wrong here
# def div_by(n,d):
#     n = int(input())
#     d = int(input())
#     assert n > 0 and d > 0 
#     return n % d == 0


# print(div_by(n,d))

#The error message "NameError: name 'n' is not defined" occurs because the 
#variables n and d are not defined in the scope where you are trying to use them in the print(div_by(n,d)) statement.


### correct 1 
# def div_by(n,d):
#     assert n > 0 and d > 0 
#     return n % d == 0

# n = int(input())
# d = int(input())

# print(div_by(n,d))


### correct 2 

# def div_by():
#     n = int(input())
#     d = int(input())
#     assert n > 0 and d > 0 
#     return n % d == 0

# print(div_by())



################ ultimate



def is_even(i):
    if i%2 == 0:
        return True 
    else:
        return False

# i = int(input("Please put the input da "))

# for i in range(i):
# for i in range(1, 6):
#     if is_even(i):
#         print(i, " is even ")
#     else:
#         print(i, " is odd duh")
    


for i in range(1, 20, 3):
    if is_even(i):
        print(i, " is even ")
    else:
        print(i, " is odd duh")

