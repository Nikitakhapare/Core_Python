'''
@Author: Nikita
@Date: 2022-04-04 18: 27: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 12:30:00
@Title: coin flip Program to calculate percentage of Haid vs Tail
'''

import random

def flipCoin():

    """
        Description:
            Function to calculate percentage of haid vs tail
        Parameter:
            No parameter
        Return:
            returning the percentage of Head vs Tail
    """
    no_of_flip=int(input("How Many times You want to flip coin "))
    tail=0
    head=0
    
    for i in range(no_of_flip):
        #tailPecentage=0
        coinFlip=random.randint(0,1)

        if coinFlip<0.5:
            tail+=1
            
        else:
            head+=1
          
    print("Tail Count is ",tail)
    print("Head count is,",head)
    tailPecentage=(tail/no_of_flip)*100
    headPercentage=100-tailPecentage

    return print("Percentage of head ", headPercentage, "vs Tail is ",tailPecentage)

flipCoin()



