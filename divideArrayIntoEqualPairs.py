class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        while len(nums) != 0:
            dummy = nums.pop(0)
            if dummy in nums:
                nums.pop(nums.index(dummy))
            else:
                return False
        return True
