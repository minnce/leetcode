class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist = 999999999999999
        for x in range(0,len(nums)):
            if abs(nums[x]) < abs(dist):
                dist = nums[x]
            elif nums[x]*-1 == dist and dist < 0:
                dist = nums[x]
        return dist
