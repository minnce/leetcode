class Solution(object):
    def getConcatenation(self, nums):
        final = []
        for x in range(0,len(nums)):
            final.append(nums[x])
        return nums+final
