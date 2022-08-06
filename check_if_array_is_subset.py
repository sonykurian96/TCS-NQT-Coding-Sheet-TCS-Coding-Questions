'''
Example 1:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [2,4,3,1,7,5,15]
Output: arr1[] is a subset of arr2[]

Example 2:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [4,5,2]
Output: arr1[] is not a subset of arr2[]

Example 3:
Input: arr1[]= [1,3,4,5,2]
       arr2[]= [11,12,13,15,16]
Output: arr1[] is not a subset of arr2[]
'''

input_list_A = [int(x) for x in input("Enter list of numbers ").split(',')]
input_list_B = [int(x) for x in input("Enter list of numbers ").split(',')]

set_A = set(input_list_A)
set_B = set(input_list_B)

if set_A.issubset(set_B):
    print("arr1[] is a subset of arr2[]")
else:
    print("arr1[] is not a subset of arr2[]")
