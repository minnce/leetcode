class Solution(object):
    def repeatedCharacter(self, s):
        s = list(s)
        found = []
        for x in range(0,len(s)):
            if s[x] in found:
                return s[x]
            if s[x] not in found:
                found.append(s[x])
