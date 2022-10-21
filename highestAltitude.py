class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        dummy = 0
        for x in range(0,len(gain)):
            dummy+=gain[x]
            if dummy > highest:
                highest = dummy
        return highest
