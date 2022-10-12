class Solution(object):
    def findNumbers(self, nums):
        counter=0
        for x in range(0,len(nums)):
            if len(str(nums[x]))%2 == 0:
                counter+=1
        return counter
