class Solution:
    def calPoints(self, operations: List[str]) -> int:
        fin = []
        for x in range(0,len(operations)):
            if operations[x] == "D":
                fin.append(fin[-1]*2)
            elif operations[x] == "C":
                fin.pop(-1)
            elif operations[x] == "+":
                fin.append(fin[-1]+fin[-2])
            else:
                fin.append(int(operations[x]))
        return sum(fin)
