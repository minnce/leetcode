class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = 0
        dum = 0
        pos = True
        while pos == True:
            if len(nums) == 1 or len(nums) == 0:
                return [counter,len(nums)+dum]
            popped = False
            dummy = nums.pop(0)
            try:
                dummy2 = nums.index(dummy)
            except ValueError:
                dum+=1
                continue
            nums.pop(dummy2)
            popped = True
            if popped == True:
                counter+=1
