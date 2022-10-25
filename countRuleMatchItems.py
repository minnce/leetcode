class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        final = 0
        if ruleKey == "type":
            hold = 0
        elif ruleKey == "color":
            hold = 1
        else:
            hold = 2
        if len(items) == 1:
            if items[0][hold] == ruleValue:
                return 1
        for x in range(0,len(items)):
            if items[x][hold] == ruleValue:
                final+=1
        return final
