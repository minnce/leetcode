class Solution(object):
    def mySqrt(self, x):
        for y in range(0,50000):
            if y*y == x:
                return y
            elif y*y > x:
                return y-1 
