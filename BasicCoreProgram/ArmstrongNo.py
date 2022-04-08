'''
@Author: Nikita
@Date: 2022-04-04 20: 08: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 20:08:00
@Title: Armstrong Number 
'''

def armstrong(n):
    """
        Description:
            Function to Chake Number is Armstrong Or Not
        Parameter:
            Passing number 
        Return:
            returning that Number is Armstrong or Not 
    """
    No=n
    sum=0
    while n > 0:
        digit=n%10
        sum=sum+digit*digit*digit
        n=n//10

    if No==sum:
        print("It is a Armstrong Number.")
    else:
        print("It is not a Armstrong numberS")



if __name__== '__main__':
    n=int(input("Enter the number: "))
    armstrong(n)
