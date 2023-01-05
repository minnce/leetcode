class Solution:
    def findGCD(self, nums: List[int]) -> int:
        dummy1 = nums.pop(nums.index(max(nums)))
        dummy2 = nums.pop(nums.index(min(nums)))
        for x in range(0,dummy2+1):
            if dummy1%(dummy2-x)==0 and dummy2%(dummy2-x)==0:
                return dummy2-x
