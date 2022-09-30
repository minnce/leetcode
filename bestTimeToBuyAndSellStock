class Solution(object):
    def maxProfit(self, prices):
        bestProf = -9999999
        buyDay = 99999999999999999
        sellDay = 0
        currentMax = -99999999999999999999999 - 1
        currentMin = 9999999999999999 + 1
        absBuy = 999999999999999999
        absSell = -9999999999999999999
        absSellDay = 0
        absBuyDay = 0
        for x in range(0,len(prices)):
            if prices[x] < currentMin:
                currentMin = prices[x]
                absBuy = prices[x]
                absBuyDay = x
                buyDay = x
                absSell = -999999999999999999999999999
                absSellDay = 0
            if prices[x] > absSell:
                absSellDay = x
                absSell = prices[x]
            if prices[x] >= currentMax and x > buyDay:
                sellDay = x
                currentMax = prices[x]
            if currentMax-currentMin > bestProf and buyDay < sellDay:
                bestProf = currentMax-currentMin
        if absSell-absBuy > bestProf and absSellDay > absBuyDay:
            return absSell-absBuy
        elif bestProf < 0:
            return 0
        else:
            return bestProf
