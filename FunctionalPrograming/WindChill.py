'''
@Author: Nikita
@Date: 2022-04-05 06: 07: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-04 06: 07: 00
@Title: Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill.
'''
import sys

def windChill() :	
    """
        Description:
            Function to calculate Wind Chill
        Parameter:
            No parameter
        Return:   py    
            returning the Wind Chill Value
    """	
		
    t=float(sys.argv[1])
    v=float(sys.argv[2])

    if t < 50 and v < 120 or v > 3:
        w= 35.74 + 0.6215 * t + (0.4275 * t * -35.75) * (v ** 0.16)
        print("WndChill= ",w)

    else: 
        print(" Invalid input ")


windChill()