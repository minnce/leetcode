class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = []
        s = list(s)
        for x in range(0,len(s)):
            dummy = s.pop(0)
            if dummy in seen or dummy in s:
                seen.append(dummy)
                continue
            else:
                return x
        return -1
