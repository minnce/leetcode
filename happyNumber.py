class Solution(object):
    def isHappy(self, n):
        cumuTotal = 0
        strNum = str(n)
        listNum = []
        alreadyListed = []
        test = True
        while test == True:
            listNum = []
            for x in range(0,len(strNum)):
                listNum.append(int(strNum[x]))
            cumuTotal = 0
            for x in range(0,len(listNum)):
                cumuTotal+=listNum[x]**2
            if cumuTotal == 1:
                return True
            if cumuTotal == n:
                return False
            for x in range(0,len(alreadyListed)):
                if cumuTotal == alreadyListed[x] and alreadyListed[x] != 1:
                    return False
            alreadyListed.append(cumuTotal)
            strNum = str(cumuTotal)
