class Solution:
    def isThree(self, n: int) -> bool:
        counter = 0
        for x in range(1,n+1):
            if n%x == 0:
                counter+=1
            if counter > 3:
                return False
        if counter == 3:
            return True
        return False
