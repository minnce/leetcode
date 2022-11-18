class Solution(object):
    def distributeCandies(self, candyType):
        canEat = len(candyType)/2
        candyType = list(set(candyType))
        if canEat > len(candyType):
            return len(candyType)
        return canEat
