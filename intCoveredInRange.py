class Solution(object):
    def isCovered(self, ranges, left, right):
        nums = []
        for x in range(0,len(ranges)):
            for y in range(ranges[x][0],(ranges[x][-1]+1)):
                nums.append(y)
        for x in range(left,right+1):
            if x not in nums:
                return False
        return True
