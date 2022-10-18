class Solution(object):
    def nextGreatestLetter(self, letters, target):
        letters.append(target)
        letters = set(letters)
        letters = list(letters)
        letters.sort()
        for x in range(0,len(letters)):
            if letters[x] == target:
                print(letters,x)
                try:
                    return letters[x+1]
                except IndexError:
                    return letters[0]
