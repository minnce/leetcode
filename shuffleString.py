class Solution(object):
    def restoreString(self, s, indices):
        s = list(s)
        dummy = ['dummy']*len(s)
        for x in range(0,len(s)):
            dummy[indices[x]] = s[x]
        return "".join(dummy)
