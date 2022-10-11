class Solution(object):
    def moveZeroes(self, nums):
        counter = 0
        for x in range(0,len(nums)):
            if nums[x+counter] == 0:
                nums.append(nums.pop(x+counter))
                counter-=1
