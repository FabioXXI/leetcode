#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums, val):
        while (val in nums):
            nums.remove(val)
        nums.sort()
        
# @lc code=end

