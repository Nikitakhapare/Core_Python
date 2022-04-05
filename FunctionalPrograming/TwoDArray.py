def addAndPrint2DArray (rows,cols):
    """
        Description:
            adding values in 2D Array
        Parameter:
            rows and colums
        Return:
            Returning nothing but printing and adding array
    """
    arr = []  
    for i in range(rows):  
        row = []  
        for j in range(cols):
            num = int(input("Enter the element"))  
            row.append(num)  
        arr.append(row)

    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

addAndPrint2DArray(2,3)