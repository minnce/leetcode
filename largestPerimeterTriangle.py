class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        leng = len(nums)
        for x in range(1,len(nums)-1):
            if nums[leng-x] < nums[leng-x-1] + nums[leng-x-2]:
                return nums[leng-x]+nums[leng-x-1]+nums[leng-x-2]
        return 0
        
