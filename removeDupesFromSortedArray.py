class Solution(object):
    def removeDuplicates(self, nums):
        counter = len(nums)
        hold = 0
        for x in range(0,len(nums)-1):
            if nums[x-hold] == nums[x+1-hold]:
                nums.append(nums.pop(x-hold))
                counter -= 1
                hold+=1
        return counter
