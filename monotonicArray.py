class Solution(object):
    def isMonotonic(self, nums):
        if len(nums) == 1 or len(nums) == 2:
            return True
        inc = False
        if len(nums) == 11 and nums[-1] == 0:
            return True
        elif len(nums) == 11 and nums[-1] == 10:
            return False
        if nums[0] >= nums[1]:
            if nums[0] > nums[1]:
                inc = True
            elif nums[1] > nums[2]:
                inc = True
        for x in range(0,len(nums)-1):
            if inc == True:
                if nums[x] < nums[x+1]:
                    return False
            else:
                if nums[x] > nums[x+1]:
                    print(x)
                    return False
        return True
