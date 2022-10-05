class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        for x in range(0,len(nums),2):
            if nums[x] == nums[-1]:
                return nums[-1]
            elif nums[x] != nums[x+1]:
                return nums[x]
