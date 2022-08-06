'''
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
'''

# solution
# 1) using inbuilt function
def maximum(array):
    return max(array)
    
a = [int(x) for x in input("Enter list of numbers ").split()]
print(maximum(a))
