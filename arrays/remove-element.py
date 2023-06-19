"""
Intuition
The idea here is to remove all the elements in the array nums that are not equal to the integer val and return the length of the array after the removal.

Complexity
Time complexity:
O(n)
The code requires two iterations to remove the val value from the list, which is proportional to the number of occurrences of val. Hence, the time complexity in this specific case is O(n), where n is the length of the input list nums.

Space complexity:
O(1)
The space complexity is O(1), which means it uses a constant amount of extra space. The solution only uses a single additional variable, count, to keep track of the number of removed elements. This variable requires a constant amount of space regardless of the input size.

Code:
"""

class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return (len(nums))