'''
Example 1:
Input:
 Nums = [1,2,-1,1,3,1]
Output:
 2,-1,3
Explanation:
 1 is the only element in the given array which occurs thrice in the array. -1,2,3 occurs only once and hence, these are non-repeating elements of the given array.

Example 2:
Input:
 Nums = [1,2,3]
Output:
 1,2,3
Explanation:
 All elements present in the array occur once. Hence, every element is non-repeating.
 '''

input_list = [int(x) for x in input("Enter list of numbers ").split(',')]

a = {}

for item in input_list:
    if item in a.keys():
        a[item] = a[item] + 1
    else:
        a[item] = 1
        
for key, value in a.items():
    if value == 1:
        print(key, end=',')
