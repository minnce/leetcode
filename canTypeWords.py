class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        l = text.split(" ")
        begin = len(l)
        brokenLetters = list(brokenLetters)
        for x in range(0,len(l)):
            temp = list(l[x])
            for y in range(0,len(temp)):
                if temp[y] in brokenLetters:
                    begin-=1
                    break
        return begin
