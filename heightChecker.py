class Solution(object):
    def heightChecker(self, heights):
        heights2 = []
        counter = 0
        for x in range(0,len(heights)):
            heights2.append(heights[x])
        heights2.sort()
        for x in range(0,len(heights)):
            if heights[x] != heights2[x]:
                counter+=1
        return counter
