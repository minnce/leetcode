import heapq
class Solution(object):
    def findMin(self, nums):
        heapq.heapify(nums)
        return heapq.heappop(nums)
        
