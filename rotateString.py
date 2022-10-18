class Solution(object):
    def rotateString(self, s, goal):
        s = list(s)
        goal = list(goal)
        if len(s) == 1:
            if s == goal:
                return True
            else:
                return False
        for x in range(0,len(s)):
            s.insert(0, s.pop(-1))
            if s == goal:
                return True
        return False
