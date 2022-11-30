class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target = list(target)
        pos = True
        s = list(s)
        dummy = 0
        compl = 0
        while pos == True:
            if dummy == len(target):
                compl+=1
                dummy = 0
            try:
                s.pop(s.index(target[dummy]))
                dummy+=1
            except ValueError:
                return compl
