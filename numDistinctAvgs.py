class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        fin = {"hello"}
        if len(nums) == 2:
            return 1
        while len(nums) != 0:
            try:
                dummy = nums.pop(0)
                dummy2 = nums.pop(-1)
                fin.add((float(dummy)+float(dummy2))/2)
            except ZeroDivisionError:
                break
        return len(list(fin))-1

