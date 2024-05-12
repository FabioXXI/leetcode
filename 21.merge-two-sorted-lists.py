#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        values = []
        while list1:
            values.append(list1.val)
            list1 = list1.next
        while list2:
            values.append(list2.val)
            list2 = list2.next
        values.sort()
        head = None
        prev = None
        for value in values:
            node = ListNode(value)
            if prev:
                prev.next = node
            prev = node
            if not head:
                head = node
        return head
        
# @lc code=end

