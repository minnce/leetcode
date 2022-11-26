class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        fin = 0
        for x in range(0,len(s)):
            if x%2 == 0:
                dummy = list(s[x])
                for y in range(0,len(dummy)):
                    if dummy[y] == "*":
                        fin+=1
        return fin
