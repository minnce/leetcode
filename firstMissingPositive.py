class Solution(object):
    def firstMissingPositive(self, nums):
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        counter = 0
        x=0
        if len(nums) == 1:
            if nums[0] == 1:
                return 2
            else:
                return 1
        if nums[-1] < 1:
            return 1
        while nums[x] <= 0:
            counter += 1
            x+=1
        if nums[counter] != 1:
            return 1
        for x in range(counter,len(nums)):
            try:
                if nums[x+1]!=nums[x]+1:
                    return nums[x]+1
            except IndexError:
                return nums[x]+1
