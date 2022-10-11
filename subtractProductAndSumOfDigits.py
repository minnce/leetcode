class Solution(object):
    def subtractProductAndSum(self, n):
        n = list(str(n))
        product = 1
        sums = 0
        for x in range(0,len(n)):
            product*=int(n[x])
            sums+=int(n[x])
        return product-sums
