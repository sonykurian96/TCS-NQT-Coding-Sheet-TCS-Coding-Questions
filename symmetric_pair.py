'''
Example 1:
Input: (1,2),(2,1),(3,4),(4,5),(5,4)
Output: (2,1) (5,4)
Explanation: Since (1,2) and (2,1) are symmetric pairs and (4,5) and (5,4) are symmetric pairs.

Example 2:
Input: (1,5),(2,3),(4,2),(5,1),(2,4)
Output: (2,4) (5,1)
Explanation: Since (1,5) and (2,4) are symmetric pairs and (5,1) and (4,2) are symmetric pairs.
'''

alt_list = [[1, 2], [2, 1], [3, 4], [4, 5], [5, 4]]
for outside in range(len(alt_list)):
    for inside in range(outside,len(alt_list)-1):
        if alt_list[outside][0] == alt_list[inside+1][1] and alt_list[outside][1] == alt_list[inside+1][0]:
            print(alt_list[outside])
