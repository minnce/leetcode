class Solution(object):
    def decompressRLElist(self, nums):
        final = []
        for x in range(0,len(nums),2):
            for y in range(0,nums[x]):
                final.append(nums[x+1])
        return final
