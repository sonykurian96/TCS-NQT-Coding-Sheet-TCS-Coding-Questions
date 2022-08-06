'''
Example 1:
Input: [2,4,1,3,5]
Output: 3

Example 2:
Input: [2,5,1,7]
Output: 3.5
'''

from statistics import median

input_list = [int(x) for x in input("Enter list of numbers ").split()]

print(median(input_list))
