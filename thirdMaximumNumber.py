class Solution(object):
    def thirdMax(self, nums):
        nums2 = set(nums)
        nums = list(nums2)
        nums.sort()
        try:
            return nums[-3]
        except IndexError:
            return nums[-1]
