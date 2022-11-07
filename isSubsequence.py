class Solution(object):
    def isSubsequence(self, s, t):
        s = list(s)
        counter = 0
        final = len(s)
        t = list(t)
        for x in range(0,len(t)):
            if counter == final:
                return True
            elif s[counter] == t[x]:
                counter+=1
        if counter == final:
            return True
        return False
