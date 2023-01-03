class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s2 = sentence.split(" ")
        for x in range(0,len(s2)-1):
            dummy = list(s2[x])
            dummy2 = list(s2[x+1])
            if dummy[-1] != dummy2[0]:
                return False
        dummy = list(s2[-1])
        dummy2 = list(s2[0])
        if dummy[-1] == dummy2[0]:
            return True
        return False
