class Solution:
    def interpret(self, command: str) -> str:
     command = list(command)
     final = ""
     dummy = ""
     for x in range(0,len(command)):
         dummy += command[x]
         if dummy == "G":
             final+="G"
             dummy = ""
         elif dummy == "()":
             final+="o"
             dummy = ""
         elif dummy == "(al)":
             final+="al"
             dummy = ""
     return final
