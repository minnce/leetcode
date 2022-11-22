class Solution:
    def secondHighest(self, s: str) -> int:
        s = list(s)
        final = []
        for x in range(0,len(s)):
            try:
                dummy = int(s[x])
                if dummy not in s:
                    final.append(s[x])
            except ValueError:
                continue
        final = list(set(final))
        final.sort()
        if len(final) < 2:
            return -1
        else:
            return final[-2]
