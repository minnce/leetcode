import heapq
import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        med = len(nums1)
        if med%2 == 0:
            med1 = med/2
            med2 = med1-1
            med3 = nums1[int(med1)]+nums1[int(med2)]
            med3 = float(med3)
            med3/=2
            return med3
        else:
            med1 = med/2
            math.floor(med1)
            return nums1[med1]
