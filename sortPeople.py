class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        fin = []
        sort = sorted(heights)
        for x in range(0,len(heights)):
            fin.insert(0,names[heights.index(sort[x])])
        return fin
