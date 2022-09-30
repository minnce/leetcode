class Solution(object):
    def containsDuplicate(self, nums):
        testSet = {"hi"}
        for x in range(0,len(nums)):
            testSet.add(nums[x])
            if len(testSet) != x+2:
                return True
        return False
