class Solution(object):
    def lengthOfLongestSubstring(self, s):
        currentLetters = []
        s = list(s)
        x = 0
        toPurge = 0
        longest = 0
        while x < len(s):
            toPurge = 0
            currentLetters.append(s[x])
            justAdded = currentLetters[-1]
            firstFind = 0
            for y in range(0,len(currentLetters)):
                if justAdded == currentLetters[y]:
                    firstFind += 1
                if justAdded == currentLetters[y] and firstFind == 2:
                    if currentLetters[y] == currentLetters[0]:
                        del currentLetters[0]
                        break
                    for e in range(1,len(currentLetters)):
                        if currentLetters[y] == currentLetters[e]:
                            toPurge = e+1
                            break
            for z in range(0,toPurge):
                del currentLetters[0]
            if len(currentLetters) > longest:
                longest = len(currentLetters)   
            x+=1
        return longest
