class Solution(object):
    def sortArrayByParity(self, nums):
        final = []
        for x in range(0,len(nums)):
            if nums[x]%2 == 0:
                final.insert(0,nums[x])
            else:
                final.insert(len(final),nums[x])
        return final
