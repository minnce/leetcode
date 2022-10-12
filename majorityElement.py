class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        numbers = {}
        for x in range(0,len(nums)):
            if nums[x] not in numbers:
                numbers[nums[x]] = 1
            elif nums[x] in numbers:
                numbers[nums[x]] = numbers[nums[x]]+1
        x = numbers.values()
        a = numbers.keys()
        y = max(x)
        for z in range(0,len(x)):
            if x[z] == y:
                x = z
                break
        return a[x]
