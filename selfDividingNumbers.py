class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        fin = []
        for x in range(left,right+1):
            dummy = list(str(x))
            div = True
            for y in range(0,len(dummy)):
                if int(dummy[y]) == 0 or x%int(dummy[y]) != 0:
                    div = False
                    break
            if div == True:
                fin.append(x)
        return fin
