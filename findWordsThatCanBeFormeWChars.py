class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars = list(chars)
        final = 0
        for x in range(0,len(words)):
            dummy = list(words[x])
            dummy2 = sorted(chars)
            for y in range(0,len(dummy)):
                if dummy[y] in dummy2:
                    dummy2.pop(dummy2.index(dummy[y]))
                elif dummy[y] not in dummy2:
                    break
                if y == len(dummy)-1:
                    final+=len(dummy)
        return final
