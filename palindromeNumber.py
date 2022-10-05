class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = list(y)
        a = list(y)
        a.reverse()
        return a == z
