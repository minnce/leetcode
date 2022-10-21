class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        dist = arr[1]-arr[0]
        for x in range(0,len(arr)-1):
            if arr[x+1]-arr[x] != dist:
                return False
        return True
