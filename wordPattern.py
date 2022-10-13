class Solution(object):
    def wordPattern(self, pattern, s):
        pattern = list(pattern)
        s = s.split(" ")
        print(pattern,s)
        seen = {}
        words = set()
        if len(s) != len(pattern):
            return False
        for x in range(0,len(s)):
            words.add(s[x])
            if pattern[x] in seen:
                if s[x] != seen[pattern[x]]:
                    return False
            else:
                dummy = pattern[x]
                seen[dummy] = s[x]
        final = seen.keys()
        if len(final) != len(list(words)):
            return False
        return True
