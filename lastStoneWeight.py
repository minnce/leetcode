import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        stones_inv = []
        for x in range(0,len(stones)):
            stones_inv.append(-stones[x])
        while len(stones_inv) > 1:
            heapq.heapify(stones_inv)
            temp1 = heapq.heappop(stones_inv)
            temp2 = heapq.heappop(stones_inv)
            temp3 = temp1-temp2
            if temp3 != 0:
                stones_inv.append(temp3)
        if len(stones_inv) > 0:
            return -stones_inv[0]
        else:
            return 0
