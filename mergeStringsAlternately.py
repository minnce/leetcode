class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        final = []
        if len(word1) > len(word2):
            for x in range(0,len(word2)):
                final.append(word1.pop(0))
                final.append(word2.pop(0))
        else:
            for x in range(0,len(word1)):
                final.append(word1.pop(0))
                final.append(word2.pop(0))
        if len(word1) != 0:
            for x in range(0,len(word1)):
                final.append(word1.pop(0))
        elif len(word2) != 0:
            for x in range(0,len(word2)):
                final.append(word2.pop(0))
        return "".join(final)
