class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        yes = 0
        allowed = list(allowed)
        for x in range(0,len(words)):
            dummy = list(words[x])
            pos = True
            for y in range(0,len(dummy)):
                if dummy[y] not in allowed:
                    pos = False
                    break
            if pos == True:
                yes+=1
        return yes 
