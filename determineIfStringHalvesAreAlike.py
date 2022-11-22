class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        left = 0
        right = 0
        half = int(len(s)/2)
        vowels = ["a","e","i","o","u"]
        for x in range(0,half):
            if s[x] in vowels:
                left += 1
        for y in range(half,len(s)):
            if s[y] in vowels:
                right += 1
        if left == right:
            return True
        return False
