'''
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 0
Explanation: 0 is the smallest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 5
Explanation: 5 is the smallest element in the array.
'''

# soluttion 
# 1 using inbuilt function
def minimum(array):
    return min(array)
    
a = [int(x) for x in input("Enter list of numbers ").split()]
print(minimum(a))
