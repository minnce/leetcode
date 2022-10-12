class Solution(object):
    def reversePrefix(self, word, ch):
        word = list(word)
        temp = []
        counter = 0
        found = False
        for x in range(0,len(word)):
            if found == True:
                break
            if word[x] == ch:
                for y in range(0,x+1):
                    temp.append(word.pop(x+counter))
                    counter -= 1
                found == True
                break
        temp="".join(temp)
        word="".join(word)
        return temp+word
