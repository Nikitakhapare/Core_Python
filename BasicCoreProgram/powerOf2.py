'''
@Author: Nikita
@Date: 2022-04-04 19: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 19:30:00
@Title: Power of 2
'''

def powerOf2(n):
    """
        Description:
            Function to calculate Power of 2 
        Parameter:
            Passing power value of n
        Return:
            returning power of 2 until n value
    """
    
    for i in range(n):
        print(2**i)

Num=int(input("Enter a number of time you want to calculate power"))
if (Num <= 0) or (Num > 31):
    print("Enter a Valid Range ")

else:

    powerOf2(Num) 