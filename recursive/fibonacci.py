"""
Question
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
Given n, calculate F(n).

Intuition
The idea here is to create a dummy mode and add values from the two lists in an ascending order. To do that, compare the values inside the two lists
and insert which ever is the smallest and increment the tail after the insertion.
If one of the list has more elements than the other, insert the trailing elements at the end of the new linkedlist. 


Complexity
Time complexity:
O(n),
where n refers to the number of elements in the two lists. the time complexity is O(n) because through the process of visiting, comparing and then copying the elements from the original lists, involves iterating through both lists once.

Space complexity:
O(1)
The space complexity is O(1), 

Code:
"""
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
