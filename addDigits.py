class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num
        num = list(str(num))
        while len(num) > 1:
            holderValue = 0
            for x in range(0,len(num)):
                holderValue+=int(num[x])
            num = holderValue
            num = list(str(num))
        return int(num[0])
