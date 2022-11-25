class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        for x in range(0,len(magazine)):
            if magazine[x] in ransomNote:
                ransomNote.pop(ransomNote.index(magazine[x]))
        if len(ransomNote) == 0:
            return True
        return False
