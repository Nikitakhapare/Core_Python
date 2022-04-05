'''
@Author: Nikita
@Date: 2022-04-05 07: 30: 00
@Last Modified by:Nikita
@Last Modified time: 2022-04-04 07: 30: 00
@Title: Program of Quadratic to calculate roots  
'''
a=int(input("Enter a Value od a"))
b=int(input("Enter a Value od b"))
c=int(input("Enter a Value od c"))
import math

detarminant=b*b - 4*a*c
print("detarminant ",detarminant)
          
    #quadratic equation is x= (-b(+-)Sqrt(b2-4ac)))/2a
          
if(detarminant>0) :
    root=math.sqrt(detarminant)          
    Root1=(-b + root)/(2*a)
    Root2=(-b - root )/(2*a)
              

    print("Root of the Equation is ",Root1," and ",Root2)

else:
    print("Root are imaginary")