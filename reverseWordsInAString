class Solution(object):
    def reverseWords(self, s):
        final = ""
        s = s.split(" ")
        print(s)
        for x in range(0,len(s)):
            temp = list(s[x])
            temp.reverse()
            temp = "".join(temp)
            if x!=len(s)-1:
                final+=temp+" "
            else:
                final+=temp
        return final
