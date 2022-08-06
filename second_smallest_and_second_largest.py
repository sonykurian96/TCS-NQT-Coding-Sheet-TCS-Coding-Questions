'''
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
'''

def maximum(array_list):
    array = list(set(array_list))
    array.pop(array.index(max(array)))
    if array:
        return max(array)
    return -1
    
    
def minimum(array_list):
    array = list(set(array_list))
    if array:
        array.pop(array.index(min(array)))
    if array:
        final_array = list(set(array))
        return min(final_array)
    return -1


input_value = [int(x) for x in input("Enter list of numbers ").split()]

print("Second largest : ", maximum(input_value))
print("Second Smallest : ", minimum(input_value))
