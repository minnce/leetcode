class Solution(object):
    def isUgly(self, n):
        while n > 1:
            if n%5 == 0:
                n/=5
            elif n%3 == 0:
                n/=3
            elif n%2 == 0:
                n/=2
            else:
                break
        if n == 1:
            return True
        else:
            return False
