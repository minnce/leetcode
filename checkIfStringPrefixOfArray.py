class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        lenCheck = len(list(s))
        dummy = ""
        for x in range(0,len(words)):
            dummy += words[x]
            if len(list(dummy)) > lenCheck and dummy != s:
                return False
            if dummy == s:
                return True
        return False
