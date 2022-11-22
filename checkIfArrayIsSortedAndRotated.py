class Solution:
    def check(self, nums: List[int]) -> bool:
        num = sorted(nums)
        for x in range(0,len(nums)):
            nums.append(nums.pop(0))
            if nums == num:
                return True
        return False
