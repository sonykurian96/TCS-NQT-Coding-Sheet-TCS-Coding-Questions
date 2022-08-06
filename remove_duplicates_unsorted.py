'''
Example 1:
Input: arr[]={2,3,1,9,3,1,3,9}
Output:  {2,3,1,9}

Explanation: Removed all the duplicate elements

Example 2:
Input: arr[]={4,3,9,2,4,1,10,89,34}
Output: {3,4,9,2,1,10,34,89}
Explanation: Removed all the duplicate elements
'''

input_list = [int(x) for x in input("Enter list of numbers ").split(',')]

a = {}

for item in input_list:
    if not item in a.keys():
        print(item, end=' ')
        a[item] = 1
