

def findTriplets(arr, n):
    """
        Description:
            Function to Triplet 
        Parameter:
            passing array and lenght of array as a parameter
        Return:   
            returning triplets whose sum is zero
    """	
 
    found = False
 
    # sort array elements
    arr.sort()
 
    for i in range(0, n-1):
     
        # initialize left and right
        frw = i + 1 #left
        rev = n - 1 #right
        x = arr[i]
        while (frw < rev):
         
            if (x + arr[frw] + arr[rev] == 0):
                # print elements if it's sum is zero
                print(x, arr[frw], arr[rev])
                frw+=1
                rev-=1
                found = True
             
 
            # If sum of three elements is less
            # than zero then increment in left
            elif (x + arr[frw] + arr[rev] < 0):
                frw+=1
 
            # if sum is greater than zero than
            # decrement in right side
            else:
                rev-=1
         
    if (found == False):
        print(" No Triplet Found")

n=int(input("Enter a lenght of array"))
array=[n]

for i in range(n):
    array.append(int(input("Enter a array elements : ")))

findTriplets(array,n)
