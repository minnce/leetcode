class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for x in range(len(nums1)-1,m-1,-1):
            nums1.pop(x)
        for x in range(0,n):
            print(nums2[x])
            nums1.append(nums2[x])
        nums1.sort()
        return nums1
