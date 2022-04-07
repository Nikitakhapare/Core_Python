'''
@Author: Nikita
@Date: 2022-04-06 06: 30: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-04 6: 30: 00
@Title: Gambler
'''
import random

def gambler_Game(stack,goal,trial):
    """
        Description:
            Function to play Gambler Game 
        Parameter:
            passing value of stack, goal, trial value
        Return:   
            returning percentage of win and tail
    """	
  
    
    bet=0
    noOfTimesWin=0
    for i in range(trial):
       
        win=0
        money=stack
        while money > 0 and money < goal:
           
            bet+=1
            
            check=random.randint(0,1)      # check gambeler win or loss
            if check==win:
                money+=1
            else:
                money-=1

        if money==goal:
            noOfTimesWin+=1

    winPercent=(noOfTimesWin/trial)*100
    print("Percentage of win ", winPercent)
    print("Percentage of loss ", 100-winPercent)


stack=int(input("Enter the value of Stack: "))
goal=int(input("Enter the Goal u want to acheave: "))
trial=int(input("Enter No of time u want to trial: "))
gambler_Game(stack,goal,trial)




    