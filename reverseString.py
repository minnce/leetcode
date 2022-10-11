class Solution(object):
    def reverseString(self, s):
        for x in range(1,len(s)+1):
            s.append(s.pop(-x))
        return s
