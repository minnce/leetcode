class Solution:
    def defangIPaddr(self, address: str) -> str:
        address = list(address)
        x=0
        while address:
            try:
                if address[x] == ".":
                    address.insert(x,"[")
                    address.insert(x+2,"]")
                    x+=2
                else:
                    x+=1
            except IndexError:
                break
        return "".join(address)
