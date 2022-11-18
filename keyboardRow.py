class Solution(object):
    def findWords(self, words):
        final = []
        row1 = ["q","w","e","r","t","y","u","i","o","p"]
        row2 = ["a","s","d","f","g","h","j","k","l"]
        row3 = ["z","x","c","v","b","n","m"]
        for x in range(0,len(words)):
            dummy = list(words[x].lower())
            inRange1 = True
            inRange2 = True
            inRange3 = True
            for y in range(0,len(dummy)):
                if dummy[y] not in row1:
                    inRange1 = False
                if dummy[y] not in row2:
                    inRange2 = False
                if dummy[y] not in row3:
                    inRange3 = False
                if inRange1 == False and inRange2 == False and inRange3 == False:
                    break
            if inRange1 == True:
                final.append(words[x])
            elif inRange2 == True:
                final.append(words[x])
            elif inRange3 == True:
                final.append(words[x])
        return final
