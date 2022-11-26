class Solution:
    def averageValue(self, nums: List[int]) -> int:
        fin = []
        for x in range(0,len(nums)):
            if nums[x]%2 == 0 and nums[x]%3 == 0:
                fin.append(nums[x])
        if len(fin) == 0:
            return 0
        return math.floor(sum(fin)/len(fin))
