class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for x in range(0,len(nums)):
            if nums[x] == target:
                return x
            if nums[x+1] > target:
                return x+1
