class Solution(object):
    def missingNumber(self, nums):
        numSet = set(nums)
        for x in range(0,len(nums)+1):
            numSet.add(x)
            if len(numSet) != len(nums):
                return x
