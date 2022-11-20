class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        sort = []
        evenQ = []
        oddQ = []
        for x in range(0,len(nums)):
            if nums[x] % 2 == 0:
                evenQ.append(nums[x])
            else:
                oddQ.append(nums[x])
        for y in range(0,len(nums)):
            if y % 2 == 0:
                sort.append(evenQ.pop(0))
            else:
                sort.append(oddQ.pop(0))
        return sort
