#Problem 1
def SearchA(Arr,x):
    searchedElement=[]
    for i in range(len(Arr)):
        if Arr[i]==x:
            searchedElement.append(i)
    return searchedElement        
            

x = int(input("Enter the number: "))
X = [22,2,1,7,11,13,5,2,9]
resultedArray= SearchA(X,x)
print("Index: ",resultedArray)

#Problem 2
def SearchB(Arr,x):
    indices = []
    for i in range(len(Arr)):
        if Arr[i] == x:
            indices.append(i)
    return indices

#Test the function
testarray = [22,2,1,7,11,13,5,2,9]
input = int(input("Enter the number: "))
print("Indices: ",SearchB(sorted(testarray),input))   
#Since we are looking gfor all the indexes of the element a linear search approach is still required  

#Problem 3
def Minimum(Arr, starting, ending):
    minindex = starting+1
    for i in range(starting , ending + 1):
        if Arr[i] < Arr[minindex]:
            minindex = i
    return minindex


Array = [3, 4, 7, 8, 0, 1, 23, -2, -5]
StartingIndex = 0
EndingIndex = 8
print(Minimum(Array, StartingIndex, EndingIndex))

#Problem 4
def Sort4(Arr):
     n= len(Arr)
     for i in range(n):
         minindex = i
         for j in range(i+1,n):
             if Arr[j]< Arr[minindex]:
                 minindex = j 
         Arr[i] , Arr[minindex] = Arr[minindex],Arr[i]        
     return Arr
    
    
    
 #unsorted array       
X =[100,-5,-3,101,0,1,-4,1,35,4]    
print(Sort4(X))

#Problem 5
def StringReverse(str, starting, ending):
    return str[starting:ending+1][::-1]


s = "University of Engineering and Technology Lahore"
starting = 27
ending = 39
print(StringReverse(s,starting,ending))

#Problem 6
def SumIterative(number):
    sum =0
    mod =0
    while number > 0:
        mod = number % 10
        sum += mod
        number //= 10
    return sum        
def SumRecursive(number):
    
    if number == 0:
        return 0
    else:      
        return number%10+ SumRecursive(number//10)
number = int(input())
print("Sum of digits is: ",SumRecursive(number))

#problem 7
def ColumnWise(Mat):
    sum = []  
    for i in range(len(Mat)):
        totalsum=0
        for j in range(len(Mat)):
           totalsum +=  Mat[j][i]
        sum.append(totalsum)   
    return sum    
def RowWise(Mat):
    sum =[]
    for i in range(len(Mat)):
        totalsum =0
        for j in range(len(Mat)):
            totalsum += Mat[i][j]
        sum.append(totalsum)   
    return  sum   
A = [[1,13,13],[5,11,6],[4,4,9]]
print(ColumnWise(A))         

#Problem 8
def SortedMerge(Arr1,Arr2):
    pointerToArr1 , pointerToArr2 = 0,0
    sortedArray = []
    while pointerToArr1 < len(Arr1) and pointerToArr2 < len(Arr2):
        if Arr1[pointerToArr1]<= Arr2[pointerToArr2]:
            sortedArray.append(Arr1[pointerToArr1])
            pointerToArr1+=1
        else:
            sortedArray.append(Arr2[pointerToArr2])
            pointerToArr2+=1
    while pointerToArr1 < len(Arr1):
        sortedArray.append(Arr1[pointerToArr1])
        pointerToArr1+=1            
        
    while pointerToArr2 < len(Arr2):
        sortedArray.append(Arr2[pointerToArr2])
        pointerToArr2+=1
    return sortedArray        
# Test the function
A = [0,3,4,10,11]
B = [1,8,13,24]
print("Sorted Array: ", SortedMerge(A,B))

#Problem 9
def PalindromRecursive(str):
    if len(str)<=1:
        return True
    if str[0] != str[-1]:
        return False
    return PalindromRecursive(str[1:-1])

# Test the function
inputString = input("Enter the string: ")
if PalindromRecursive(inputString):
    print("Palindrome") 
else:
    print("Not a palindrome")        

#Problem 10
def Sort10(Arr):
     negatives = sorted([x for x in Arr if x < 0])
     non_negatives = sorted([x for x in Arr if x>=0])
     i,j = 0,0
     result = []
     while i < len(negatives) and j < len(non_negatives):
         result.append(negatives[i])
         result.append(non_negatives[j])
         i+=1
         j+=1
     if i < len(negatives):
         result.extend(negatives[i:])
     if j < len(non_negatives):
         result.extend(non_negatives[j:])         
     return result             
#Test the function
A =  [10, -1, 9, 20, -3, -8, 22, 9, 7]
print ("Sorted Array: ",Sort10(A))    