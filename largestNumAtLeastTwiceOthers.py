class Solution(object):
    def dominantIndex(self, nums):
        largest = nums.index(max(nums))
        nums = sorted(nums)
        if nums[-1] >= nums[-2]*2:
            return largest
        return -1
