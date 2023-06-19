"""
Question
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
-----------------------------------
Intuition
In order to concatenate the array with itself, the easiest route is by mutiplying itself by two.

Complexity
Time complexity:
O(n),
where n refers to the number of elements in the list, as it involves multiplying itself,  time is proportional to the size of the input array.

Space complexity:
O(n)
The space complexity is O(n), because the resulting array is the multiplication of the input array. The space is proportional to the size of the input array.

Code:
"""


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = nums*2
        return ans