class Solution(object):
    def sortedSquares(self, nums):
        final = []
        for x in range(0,len(nums)):
            placeHolder = (nums[x]**2)
            final.append(placeHolder)
        final.sort()
        return final
