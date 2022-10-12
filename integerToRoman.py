class Solution(object):
    def intToRoman(self, num):
        final = ""
        while num != 0:
            print(final)
            if num-1000 >= 0:
                num-=1000
                final+="M"
                continue
            elif num-900 >= 0:
                num-=900
                final+="CM"
                continue
            elif num-500 >= 0:
                num-=500
                final+="D"
                continue
            elif num-400 >= 0:
                num-=400
                final+="CD"
                continue
            elif num-100 >= 0:
                num-=100
                final+="C"
                continue
            elif num-90 >= 0:
                num-=90
                final+="XC"
                continue
            elif num-50 >= 0:
                num-=50
                final+="L"
                continue
            elif num-40 >= 0:
                num-=40
                final+="XL"
                continue
            elif num-10 >= 0:
                num-=10
                final+="X"
                continue
            elif num-9 >= 0:
                num-=9
                final+="IX"
                continue
            elif num-5 >= 0:
                num-=5
                final+="V"
                continue
            elif num-4 >= 0:
                num-=4
                final+="IV"
                continue
            else:
                num-=1
                final+="I"
                continue
        return final
