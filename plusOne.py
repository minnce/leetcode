class Solution(object):
    def plusOne(self, digits):
        strDig = ""
        for x in range(0,len(digits)):
            strDig+=str(digits[x])
        intDig = int(strDig)+1
        strDig = str(intDig)
        final = []
        for x in range(0,len(strDig)):
            final.append(int(strDig[x]))
        return final
