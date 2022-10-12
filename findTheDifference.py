class Solution(object):
    def findTheDifference(self, s, t):
        s = list(s)
        s.sort()
        t = list(t)
        t.sort()
        for x in range(0,len(s)):
            if s[x] != t[x]:
                return t[x]
        return t[-1]
