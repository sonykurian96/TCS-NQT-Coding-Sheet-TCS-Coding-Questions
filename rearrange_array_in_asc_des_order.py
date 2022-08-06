'''
Example 1:
Input: 8 7 1 6 5 9
Output: 1 5 6 9 8 7
Explanation: First three elements are in the ascending order and next three elements are in the descending order.

Example 2:
Input: 4 2 8 6 15 5 9 20
Output: 2 4 5 6 20 15 9 8
'''

input_list = [int(x) for x in input("Enter list of numbers ").split()]

input_list.sort()

for index in range(0, int(len(input_list)/2)):
    print(input_list[index], end=' ')
    
input_list.sort(reverse=True)
    
for index in range(0, int(len(input_list)/2)):
    print(input_list[index], end=' ')
