'''
@Author: Nikita
@Date: 2022-04-04 20: 30: 00
@Last Modified by: Nikita
@Last Modified time: 2022-04-04 20:30:00
@Title: Fibbonacci Series 
'''
def fibonacciSeries(n):
    """
        Description:
            Function to print Fibbonacci Series
        Parameter:
            Passing nth value as a parameter
        Return:
            returning Febonnacci Series
    """
    n1=0
    n2=1
    print("Fibbonacci Series is ",n,"Term is ")
    print(n1," ",n2, " ", end= "")
    for i in range (2,n+1):
        temp=n1+n2
        print("",temp , end=" ")
        n1=n2
        n2=temp

if __name__== '__main__':
    n=int(input("Enter value of n: "))
    fibonacciSeries(n)


