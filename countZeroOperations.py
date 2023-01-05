class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        if num1 == num2 and num1 == 0:
            return 0
        if num1 == 0 or num2 == 0:
            return 0 
        while num1 != num2:
            if num1 > num2:
                num1 = num1-num2
                counter+=1
            elif num1 < num2:
                num2 = num2-num1
                counter+=1
        return counter+1
            
