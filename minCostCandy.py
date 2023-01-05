class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        total = 0
        counter = 0
        while len(cost) > 0:
            dummy=cost.pop(cost.index((max(cost))))
            total+=dummy
            counter+=1
            if counter == 2:
                try:
                    dummy=cost.pop(cost.index(max(cost)))
                    counter=0
                except ValueError:
                    continue
        return total
