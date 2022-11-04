class Solution(object):
    def threeConsecutiveOdds(self, arr):
        if len(arr) < 3:
            return False
        for x in range(0,len(arr)-2):
            if arr[x]%2 == 1 and arr[x+1]%2 == 1 and arr[x+2]%2 == 1:
                return True
        return False
