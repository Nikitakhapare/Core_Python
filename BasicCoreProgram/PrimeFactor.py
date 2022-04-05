'''
@Author: Nikita
@Date: 2022-04-04 21 : 45: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 21:45:00
@Title: Power of 2
'''
import re


def primefactor(n):
    """
        Description:
            Function to Calculate Prime Factors
        Parameter:
            Passing number n 
        Return:
            returning prime Factors of n value
    """
    factors=[]
    i=2
    while(i <= n):
        if(n % i == 0):
            factors.append(i)
            n=n/i
            
        else:
            i+=1 

    return factors   

n = int(input("Enter any Number for calculating the prime factors: "))
print(primefactor(n))