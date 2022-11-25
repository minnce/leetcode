class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        fin = []
        for x in range(0,len(nums1)):
            for y in range(nums2.index((nums1[x])),len(nums2)):
                if nums2[y] > nums1[x]:
                    fin.append(nums2[y])
                    break
                elif y == len(nums2)-1:
                    fin.append(-1)
        return fin
