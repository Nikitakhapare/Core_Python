'''
@Author: Nikita
@Date: 2022-04-06 06: 30: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-07 12: 10: 00
@Title: Coupon Numbers
'''

import random

def distinct_coupen_generator(n):
    """
        Description:
            Function to Generate Distinct Coupon Number
        Parameter:
            passing vvalue of No of Coupon Digit
        Return:   
            returning Distinct Coupon Number
    """	
    list=[]
    i=1
    while i<(n+1):
        rand = random.randint(0,9)
        if rand in list: 
            i-=1
        else:
            list.append(rand)
        
        i+=1
    print("Cupon Code is ", list)
    


n =int(input("Enter how many digit of coupon codes you need: "))
distinct_coupen_generator(n)