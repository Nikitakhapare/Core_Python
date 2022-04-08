'''
@Author: Nikita
@Date: 2022-04-04 20: 57: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 20:57:00
@Title:Largest Number Among Three
'''

def largest_no(num1,num2,num3):
    """
        Description:
            Function to Chake Largest Number among Three Number
        Parameter:
            Passing numbers as a Parameter
        Return:
            returning Largest Number
    """
   
    if (num1 >= num2) and (num1 >= num3):
        largest = num1

    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print("The largest number is", largest)

if __name__== '__main__':
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))
    largest_no(num1,num2,num3)