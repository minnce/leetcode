class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        most = -1
        dummy = 1
        currNum = 999999
        nums.sort()
        ev = False
        for x in range(0,len(nums)):
            if nums[x-1] == nums[x] and nums[x]%2==0:
                ev = True
                dummy+=1
            else:
                dummy = 1
            if dummy > most:
                most = dummy
                currNum = nums[x]
            elif dummy == most:
                if nums[x] < currNum:
                    currNum = nums[x]
        if ev == False:
            for x in range(0,len(nums)):
                if nums[x]%2 == 0:
                    return nums[x]
            return -1
        else:
            return currNum
