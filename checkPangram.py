class Solution(object):
    def checkIfPangram(self, sentence):
        needed = set()
        sen = list(sentence)
        for x in range(0,len(sen)):
            if sen[x] not in needed:
                needed.add(sen[x])
            if len(needed) == 26:
                return True
        return False
