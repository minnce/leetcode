class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        final = ""
        final2 = ""
        for x in range(0,len(word1)):
            final+=word1[x]
        for x in range(0,len(word2)):
            final2+=word2[x]
        return final == final2
