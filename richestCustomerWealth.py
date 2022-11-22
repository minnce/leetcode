class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        final = []
        for x in range(0,len(accounts)):
            final.append(sum(accounts[x]))
        final.sort()
        return final[-1]
