class Solution(object):
    def findMaxK(self, nums):
        largest = -1
        for x in range(0,len(nums)):
            if nums[x] > largest and -nums[x] in nums:
                largest = nums[x]
        return largest
