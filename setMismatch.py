class Solution(object):
    def findErrorNums(self, nums):
        itr = len(nums)
        nums.sort()
        repeat = None
        missing = None
        for x in range(1,itr+1):
            if x not in nums:
                missing = x
        for y in range(0,len(nums)-1):
            if nums[y] == nums[y+1]:
                repeat = nums[y]
                return [repeat, missing]
