class Solution(object):
    def findComplement(self, num):
        num = list(bin(num))
        for y in range(0,2):
            del num[y]
        final = ""
        for x in range(0,len(num)):
            if num[x] == '0':
                final+="1"
            else:
                final+="0"
        print(final)
        return int(final,2)
