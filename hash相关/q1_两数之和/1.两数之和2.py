#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]+nums[j]==target):
                    return [i ,j]
        '''
        hashmap ={}
        for i in range(len(nums)):
            if target- nums[i] in hashmap:
                return [hashmap[target- nums[i]],i]
            else:
                hashmap[nums[i]]=i
        
# @lc code=end

