class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        fin = -1
        curr = 0
        for x in range(0,len(nums)):
            if nums[x] == 1:
                curr += 1
            if curr > fin:
                fin = curr
            if nums[x] != 1:
                curr = 0
        return fin
