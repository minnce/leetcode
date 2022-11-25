class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fin = []
        if len(nums1) > len(nums2):
            for x in range(0,len(nums1)):
                if nums1[x] in nums2:
                    fin.append(nums1[x])
                    nums2.pop(nums2.index(nums1[x]))
            return fin
        else:
            for y in range(0,len(nums2)):
                if nums2[y] in nums1:
                    fin.append(nums2[y])
                    nums1.pop(nums1.index(nums2[y]))  
            return fin
