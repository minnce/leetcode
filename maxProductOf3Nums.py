class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        testMax = nums[-1]*nums[-2]*nums[-3]
        testMax2 = nums[0]*nums[1]*nums[-1]
        if testMax > testMax2:
            return testMax
        return testMax2
