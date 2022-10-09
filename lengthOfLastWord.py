class Solution(object):
    def lengthOfLastWord(self, s):
        x = s.split(" ")
        if len(x) == 1:
            return len(list(s))
        for z in range(len(x)-1,-1,-1):
            if x[z].isalnum() == True:
                y = list(x[z])
                return len(y)
