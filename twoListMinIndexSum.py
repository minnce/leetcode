class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        best = 10000000000000000000000000000
        final = []
        if len(list1) > len(list2):
            for x in range(0,len(list1)):
                if list1[x] in list2 and x+list2.index(list1[x]) < best:
                    best = x+list2.index(list1[x])
                    final = [list1[x]]
                elif list1[x] in list2 and x+list2.index(list1[x]) == best:
                    final.append(list1[x])
        else:
            for x in range(0,len(list2)):
                if list2[x] in list1 and x+list1.index(list2[x]) < best:
                    best = x+list1.index(list2[x])
                    final = [list2[x]]
                elif list2[x] in list1 and x+list1.index(list2[x]) == best:
                    final.append(list2[x])
        return final
