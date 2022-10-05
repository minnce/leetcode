class Solution(object):
    def isPerfectSquare(self, num):
        for x in range(0,50000):
            if x*x == num:
                return True
        return False
