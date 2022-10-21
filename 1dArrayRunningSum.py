class Solution(object):
    def runningSum(self, nums):
        final = []
        dummy = 0
        for x in range(0,len(nums)):
            dummy+=nums[x]
            final.append(dummy)
        return final
