class Solution(object):
    def findSpecialInteger(self, arr):
        dummy = 1
        if len(arr) == 1:
            return arr[0]
        for x in range(0,len(arr)-1):
            if arr[x] == arr[x+1]:
                dummy+=1
            else:
                dummy = 1
            if dummy>len(arr)/4:
                return arr[x]
