class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for x in range(0,len(numbers)):
            compliment = target-numbers[x]
            if compliment in seen:
                return [seen[compliment]+1,x+1]
            seen[numbers[x]] = x 
