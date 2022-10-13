class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() == True:
            return True
        elif word.islower() == True:
            return True
        word = list(word)
        if word.pop(0).isupper() == False:
            return False
        word = "".join(word)
        if word.islower() == True:
            return True
