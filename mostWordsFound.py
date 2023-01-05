class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        longest = 0
        for x in range(0,len(sentences)):
            dummy = sentences.pop(0)
            dummy2 = len(dummy.split(" "))
            if dummy2 > longest:
                longest = dummy2
        return longest
