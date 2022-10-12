class Solution(object):
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)
        c = str(a+b)
        c = list(bin(int(c)))
        c.pop(0)
        c.pop(0)
        c = "".join(c)
        return c
