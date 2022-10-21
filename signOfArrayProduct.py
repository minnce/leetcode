class Solution(object):
    def arraySign(self, nums):
        product = 1
        for x in range(0,len(nums)):
            product*=nums[x]
        if product == 0:
            return 0
        elif product > 0:
            return 1
        else: return -1
