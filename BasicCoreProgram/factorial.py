'''
@Author: Nikita
@Date: 2022-04-04 19: 15: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 19:15:00
@Title: Factorial of Number 
'''

def factorial(n):
    """
        Description:
            Function to calculate Factorial of Number
        Parameter:
            Passing Number As a Parameter
        Return:
            returning the Factorial Of Number
    """
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i

    print("Factorial of Giver No is : ",factorial)
    
if __name__ == '__main__':
    n=int(input("Enter the Number : "))
    factorial(n)