class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        finals = []
        currMin = 9999999999999999999999999999999999999999999999999
        x = 0
        while x != len(arr)-1:
            dummy = abs(arr[x+1]-arr[x])
            if dummy < currMin:
                finals = []
                finals.append([arr[x],arr[x+1]])
                currMin = dummy
            elif dummy == currMin:
                finals.append([arr[x],arr[x+1]])
            x+=1
        return finals
