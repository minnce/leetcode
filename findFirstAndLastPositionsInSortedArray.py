class Solution(object):
    def searchRange(self, nums, target):
        location1 = -1
        location2 = -1
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
        for x in range(0,len(nums)):
            if nums[x] == target and location1 == -1:
                location1 = x
            if nums[x] == target:
                location2 = x
        return [location1, location2]
