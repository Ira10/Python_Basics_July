import sys
def areaRec(length,breadth):
    '''
    Objective is to compute the area of a rectangle
    using length and breadth
    '''
    area = length * breadth
    return area 

def main():
    # print('Enter the following values to get the area')
    # lengthRect = int(input("Enter the length "))
    # breadthRect = int(input("Enter the breadth "))
    # areaRect_ = areaRec(lengthRect, breadthRect)
    # return areaRect_
    if len(sys.argv) == 3:
        lengthRect = int(sys.argv[1])
        breadthRect = int(sys.argv[2])  
        areaRect_ = areaRec(lengthRect, breadthRect)
        print("Area of rectangle is ", areaRect_)
    else:
        print("Unexpected number of command line arguments")

# print(main()) ### this will work 

if __name__ == '__main__':
    main()

print('End of program \n')

'''
To get the result of the program, do this ------

(base) indrani.sarkar@HO-002-LP-00389 Python Basics - July % python 16th_July_Command_line_arg_book.py 10 23
Area of rectangle is  230
End of program 

(base) indrani.sarkar@HO-002-LP-00389 Python Basics - July % 
'''