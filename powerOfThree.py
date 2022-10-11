class Solution(object):
    def isPowerOfThree(self, n):
        for x in range(-20,20):
            if 3**x == n:
                return True
        return False
