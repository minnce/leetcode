class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        fin = []
        for x in range(0,len(arr2)):
            try:
                while arr1.index(arr2[x])==0 or arr1.index(arr2[x]):
                    fin.append(arr1.pop(arr1.index(arr2[x])))
            except ValueError:
                continue
        arr1.sort()
        return fin+arr1
