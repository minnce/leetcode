class Solution(object):
    def countDigits(self, num):
        num2 = list(str(num))
        fin = 0
        for x in range(0,len(num2)):
            if num%int(num2[x]) == 0:
                fin+=1
        return fin
