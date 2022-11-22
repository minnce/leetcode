class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
            k = int(math.floor(n/2))
            matches += k
            n = n-k
        return matches
