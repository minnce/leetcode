class Solution(object):
    def romanToInt(self, s):
        s = list(s)
        final = 0
        while len(s) >= 1:
            if len(s) >= 2:
                if s[0]+s[1] == "CM":
                    final+=900
                    del s[0]
                    del s[0]
                    continue
                elif s[0]+s[1] == "CD":
                    final+=400
                    del s[0]
                    del s[0]
                    continue
                elif s[0]+s[1] == "XC":
                    final+=90
                    del s[0]
                    del s[0]
                    continue
                elif s[0]+s[1] == "XL":
                    final+=40
                    del s[0]
                    del s[0]
                    continue
                elif s[0]+s[1] == "IX":
                    final+=9
                    del s[0]
                    del s[0]
                    continue
                elif s[0]+s[1] == "IV":
                    final+=4
                    del s[0]
                    del s[0]
                    continue
            if s[0] == "M":
                final+=1000
                del s[0]
                continue
            elif s[0] == "D":
                final+=500
                del s[0]
                continue
            elif s[0] == "C":
                final+=100
                del s[0]
                continue
            elif s[0] == "L":
                final+=50
                del s[0]
                continue
            elif s[0] == "X":
                final+=10
                del s[0]
                continue
            elif s[0] == "V":
                final+=5
                del s[0]
                continue
            elif s[0] == "I":
                final+=1
                del s[0]
                continue
        
        return final

