class Solution(object):
    def judgeCircle(self, moves):
        uCount = 0
        dCount = 0
        lCount = 0
        rCount = 0
        moves = list(moves)
        for x in range(0,len(moves)):
            if moves[x] == "U":
                uCount+=1
            elif moves[x] == "D":
                dCount+=1
            elif moves[x] == "L":
                lCount+=1
            else:
                rCount+=1
        if uCount == dCount and lCount == rCount:
            return True
        else:
            return False
