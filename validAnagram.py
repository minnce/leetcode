class Solution(object):
    def isAnagram(self, s, t):
        tryAgain = False
        test = list(s)
        test2 = list(t)
        for x in range (0,len(test)):
            if tryAgain == True:
                x=0
            for y in range(0,len(test2)):
                try:
                    if test[x] == test2[y]:
                        del test[x]
                        del test2[y]
                        print(test[x],test2[y])
                except:
                    IndexError
                    tryAgain = True
                    break
        if len(test) == 0 and len(test2) == 0 or test==test2:
            return True
        else:
            return False
