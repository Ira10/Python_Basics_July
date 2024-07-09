def areaRec(length,breadth):
    '''
    Objective is to compute the area of a rectangle
    using length and breadth
    '''
    area = length * breadth
    return area 

def main():
    print('Enter the following values to get the area')
    lengthRect = int(input("Enter the length "))
    breadthRect = int(input("Enter the breadth "))
    areaRect_ = areaRec(lengthRect, breadthRect)
    return areaRect_

print(main()) ### this will work 

# if __name__ == '__main__':
#     main()

# print('End of program \n')