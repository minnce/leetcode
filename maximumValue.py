class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        curr = 0
        for x in range(0,len(strs)):
            if strs[x].isnumeric() == True:
                dummy = int(strs[x])
                if dummy > curr:
                    curr = dummy
            else:
                dummy = len(list(strs[x]))
                if dummy > curr:
                    curr = dummy
        return curr
