class Solution:
    def pivotInteger(self, n: int) -> int:
        dummy = []
        if n == 1:
            return 1
        for x in range(1,n+1):
            dummy.append(x)
        sumR = sum(dummy)
        sumL = 0
        x = 1
        while sumL < sumR and x < n:
            sumL+=x
            sumR-=x
            if sumL == sumR-x-1:
                return x+1
            x+=1
        return -1
