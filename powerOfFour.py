class Solution(object):
    def isPowerOfFour(self, n):
        for x in range(0,17):
            if 4**x == n:
                return True
        return False
