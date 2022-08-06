'''
Example:
Input: N = 5, array[] = {1,2,3,4,5}
insertbeginning(6)
insertending(7)
insertatpos(8,4)
Output: 6,1,2,8,3,4,5,7
Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4
'''

from collections import deque
input_list = [int(x) for x in input("Enter list of numbers ").split(',')]

d = deque(input_list)

def insertbeginning(array, element):
    array.appendleft(element)
    return array
    
def insertending(array, element):
    array.append(element)
    return array
    
def insertatpos(array, element, pos):
    array.insert(pos, element)
    return array
    

insertbeginning(d,9)
insertending(d,1)
print(list(insertatpos(d,7, 2)))
