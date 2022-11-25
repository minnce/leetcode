class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        trans = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        fin = {"bruh"}
        for x in range(0,len(words)):
            dummy = []
            dummy2 = list(words[x])
            for y in range(0,len(dummy2)):
                dummy.append(trans[dummy2[y]])
            fin.add("".join(dummy))
        return len(list(fin))-1
