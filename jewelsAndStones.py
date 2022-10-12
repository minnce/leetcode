class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels = list(jewels)
        stones = list(stones)
        counter = 0
        for x in range(0,len(stones)):
            if stones[x] in jewels:
                counter+=1
        return counter
