'''
Example 1:
Input: 
Arr[] = [1,1,2,3,4,4,5,2]
Output:
 1,2,4
Explanation:
 1,2 and 4 are the elements which are occurring more than once.

Example 2:
Input:
 Arr[] = [1,1,0]
Output:
 1
Explanation:
 Only 1 is occurring more than once in the given array.
 '''

input_list = [int(x) for x in input("Enter list of numbers ").split(',')]

a = {}

for item in input_list:
    if item in a.keys():
        print(item, end=',')
    else:
        a[item] = 1
