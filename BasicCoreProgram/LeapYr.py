'''
@Author: Nikita
@Date: 2022-04-04 18: 27: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 18:27:00
@Title: Leap Year
'''

def LeapYrChecker(yr):
    """
        Description:
            Function to calculate Year is Leap or Not 
        Parameter:
            Passing a Year as a parameter 
        Return:
            returning that Entered Year is Leap year or Not 
    """
    
    if (yr%4)==0:

        if (yr%100)==0:

            if(yr%400)==0:
                print("Its a Leap year")

            else:
                print("Its not a Leap year")
        
        else:
            print("It is a Leap year")

    else:
        print("Its Not a Leap year")

year=int(input("Enter a Year you want to check : "))
if year >9999 or year < 1000:
    print("Enter a Four Digit Year")

else: 
    LeapYrChecker(year)