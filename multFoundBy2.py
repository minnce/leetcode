class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while True:
            try:
                nums.index(original)
                original*=2
            except ValueError:
                return original
