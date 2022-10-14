class Solution(object):
    def reverse(self, x):
        Neg = False
        if x < 0:
            Neg = True
        x = list(str(x))
        if Neg == True:
            x.pop(0)
        x.reverse()
        while x[0] == 0:
            x.pop(0)
        x="".join(x)
        x=int(x)
        if Neg == True:
            x*=-1
        if x < -2**31 or x > 2**31-1:
            return 0
        return x
