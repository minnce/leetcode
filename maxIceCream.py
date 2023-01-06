class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cost = sorted(costs)
        counter = 0
        for x in range(0,len(cost)):
            if coins >= cost[x]:
                coins-=cost[x]
                counter+=1
            else:
                return counter
        return counter
