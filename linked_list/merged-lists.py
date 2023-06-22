"""
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
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        tail.next = list1 or list2
        return dummy.next

