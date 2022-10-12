class Solution(object):
    def intersection(self, nums1, nums2):
        final = []
        found = set(nums1)
        nums2 = set(nums2)
        nums2 = list(nums2)
        for x in range(0,len(nums2)):
            if nums2[x] in found:
                final.append(nums2[x])
        return final
