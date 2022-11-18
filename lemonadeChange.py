class Solution(object):
    def lemonadeChange(self, bills):
        bill = [0,0,0]
        for x in range(0,len(bills)):
            if bills[x] == 5:
                bill[0] = bill[0]+1
            if bills[x] == 10:
                if bill[0] == 0:
                    return False
                else:
                    bill[0] = bill[0]-1
                    bill[1] = bill[1]+1
            if bills[x] == 20:
                if bill[1] >= 1 and bill[0] >= 1:
                    bill[0] = bill[0]-1
                    bill[1] = bill[1]-1
                    bill[2] = bill[2]+1
                elif bill[0] >= 3:
                    bill[0] = bill[0]-3
                    bill[2] = bill[2]+1
                else:
                    return False
        return True
