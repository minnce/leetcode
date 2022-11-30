class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        password = list(password)
        if len(password) < 8:
            return False
        up = False
        low = False
        num = False
        spec = False
        dummy = ["!","@","#","$","%","^","&","*","(",")","-","+"]
        for x in range(0,len(password)):
            if password[x].isupper() == True:
                up = True
            if password[x].islower() == True:
                low = True
            if password[x].isnumeric() == True:
                num = True
            if password[x] in dummy:
                spec = True
            try:
                print(password[x],password[x+1])
                if password[x] == password[x+1]:
                    return False
            except IndexError:
                print("no")
        if up == True and low == True and spec == True and num == True:
            return True
        return False
