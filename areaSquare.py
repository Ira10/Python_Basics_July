def areaRec(length,breadth):
    '''
    Objective is to compute the area of a rectangle
    using length and breadth
    '''
    area = length * breadth
    return area 

def areaSquare(side):
    areaSquare = areaRec(side,side)
    return areaSquare

def main():
    print('Enter the following values to get the area')
    lengthRect = int(input("Enter the length "))
    breadthRect = int(input("Enter the breadth "))
    areaRect_ = areaRec(lengthRect, breadthRect)
    print('Area of a rectangle is', areaRect_)
    print('\n')
    sideSqr = int(input("Enter the side of a square "))
    areaSqr_ = areaSquare (sideSqr)
    print('Area of a square is', areaSqr_)
    print("\n The end of the program")

# print(main()) 
'''
why is it printing none in the end :: The main() function is being called with print(main()). In Python, print() outputs the return value of the function it's given, and main() does not explicitly return any value, so it returns None by default. Therefore, print(main()) prints None after executing the main() function.
'''

main()