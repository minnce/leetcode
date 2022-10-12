class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        counter = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                counter+=1
            return counter >= n
        for x in range(0,len(flowerbed)):
            if x == 0:
                if flowerbed[1] == 0 and flowerbed[0] == 0:
                    counter+=1
                    flowerbed[x] = 1
            elif x == len(flowerbed)-1:
                if flowerbed[x-1] == 0 and flowerbed[x] == 0:
                    counter+=1
                    flowerbed[x] = 1
            elif flowerbed[x-1] == 0 and flowerbed[x+1] == 0 and x!=0 and x!=len(flowerbed)-1 and flowerbed[x] != 1:
                counter+=1
                flowerbed[x] = 1
        print(flowerbed)
        return counter >= n
