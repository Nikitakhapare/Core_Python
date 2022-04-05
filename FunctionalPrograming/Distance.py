'''
@Author: Nikita
@Date: 2022-04-05 06: 30: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-04 06: 30: 00
@Title: Calculate Distance between of x and y co-ordinate from origin
'''
import math

x1=0
x2=0

x2=int(input("Enter x co-ordinate"))
y2=int(input("Enter y co-ordinate"))

Distance= math.sqrt((x2 * x2) * (y2 * y2))
print("Distance Between two co-ordinates is : ", Distance)