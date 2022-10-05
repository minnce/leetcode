class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        if n > 0:
            for x in range(0,32):
                if 2**x == n:
                    return True
            return False
