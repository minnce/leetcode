class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = {}
        s = list(s)
        t = list(t)
        for x in range(0,len(s)):
            if s[x] in seen and seen[s[x]] != t[x]:
                return False
            seen[s[x]] = t[x]
        x = list(seen.values())
        while len(x) != 0:
            dummy = x.pop(0)
            if dummy in x:
                return False
        return True
