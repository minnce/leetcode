class Solution(object):
    def longestCommonPrefix(self, strs):
        final = ""
        onGoing = True
        for x in range(0,len(strs)):
            shortest = min(len(strs[x]),300)
        print(shortest)
        for x in range(0,shortest):
            try:
                dummy = strs[0][x]
            except IndexError:
                break
            for y in range(0,len(strs)):
                try:
                    if strs[y][x] != dummy:
                        onGoing = False
                        break
                except IndexError:
                    onGoing = False
                    break
            if onGoing == False:
                break
            final+=dummy
        return final
