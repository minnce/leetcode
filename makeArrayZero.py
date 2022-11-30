class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        test = True
        holder = 0
        while test == True:
            try:
                dummy = min(nums)
                if dummy == 0:
                    nums.pop(nums.index(dummy))
                    continue
                for x in range(0,len(nums)):
                    nums[x]-=dummy
                holder+=1
            except ValueError:
                return holder
            
        
