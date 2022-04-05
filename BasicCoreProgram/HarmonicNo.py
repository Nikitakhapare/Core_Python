'''
@Author: Nikita
@Date: 2022-04-04 19: 45: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 12:30:00
@Title: Harmonic of n
'''
def harmonicNo(n):
    """
        Description:
            Function to nth Harmonic Value
        Parameter:
            Passing n for which Harmonic value to be calculate
        Return:
            returning the printing statment along with nth Harmonic value
    """
    harmonic=0     #H[1]=1/1=1
    for i in range(1,n):
        harmonic=harmonic+1/i
        
    return print("nth Harmonic value is ",harmonic)
    

Num=int(input("Enter a n for which u want to calculate Harmonic value: "))
harmonicNo(Num)