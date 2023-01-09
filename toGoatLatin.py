class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        final = ""
        sen = sentence.split(" ")
        for x in range(0,len(sen)):
            dummy = list(sen[x])
            if dummy[0] == "a" or dummy[0] == "e" or dummy[0] == "i" or dummy[0] == "o" or dummy[0] == "u" or dummy[0] == "A" or dummy[0] == "E" or dummy[0] == "I" or dummy[0] == "O" or dummy[0] == "U":
                dummy.append("ma")
            else:
                dummy2 = dummy.pop(0)
                dummy.append(dummy2)
                dummy.append("ma")
            dummy.append("a"*(x+1))
            final+="".join(dummy)
            if x != len(sen)-1:
                final+=" "
        return final
