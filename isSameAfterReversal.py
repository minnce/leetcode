class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num2=list(str(num))
        num2.reverse()
        num3=int("".join(num2))
        num4=list(str(num3))
        num4.reverse()
        num5=int("".join(num4))
        if num == num5:
            return True
        return False
